import os
import sys
from pathlib import Path
from typing import Dict, List, Union

import requests

from src.classes.session import Session
from src.helpers.listings import get_list
from src.helpers.print_functions import print_error, print_file, print_warning
from src.helpers.url import get_url
from src.helpers.utils import is_file
from src.variables import CA_BUNDLE, DOWNLOAD_FILE_URL, LIST_RECURSIVE


def _get_file_names(files: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    "Function to extract names from a list of files"
    file_names = {}
    for file in files:
        file_names[file["name"]] = file
    return file_names


def expand_directory(
    tree: Dict, target: str, recursive, proceed: bool = True, base_path=""
):
    "Function to walk a directory and retrieve its filenames"
    files = []
    if isinstance(tree, dict) and "data" in tree:
        for item in tree["data"]:
            files.extend(expand_directory(item, target, recursive, base_path=base_path))
        return files
    current_path = Path(f"{base_path}/{tree['name']}".lstrip("/")).as_posix()
    if not tree.get("children"):
        files.append(current_path)
        return files
    if recursive or proceed:
        # If is not recursive should only download first level of target directory
        proceed = not (proceed and current_path == target)
        for child in tree["children"]:
            files.extend(
                expand_directory(child, target, recursive, proceed, current_path)
            )

    return files


def _expand_requested(session, requested: List[str]) -> List[str]:
    expanded = []
    for file in requested:
        if not is_file(file):
            response = requests.get(
                session.options.host + LIST_RECURSIVE + session.options.project,
                cookies=session.cookies,
                params={"cd": Path(f"{session.options.project}/{file}").as_posix()},
                verify=CA_BUNDLE,
            )
            if response.status_code == 404:
                print_error(
                    "No available files to download under that directory, make sure directory is correct or files have not expired"
                )
                sys.exit(1)
            expanded.extend(
                expand_directory(
                    response.json(),
                    Path(f"{session.options.project}/{file}").as_posix(),
                    session.options.recursive,
                )
            )
        else:
            expanded.append(Path(f"{session.options.project}/{file}").as_posix())

    return expanded


def download(session: Session) -> None:
    """
        Verify the files specified with the download command and passes the approved files to the get url.
    :param session: The session object.
    :return: None
    """
    if session.options.project is None:
        print_error("No project provided")
        sys.exit(1)
    if (
        session.options.dir.split("/")[0] != session.options.project
        and session.options.dir != "./"
    ):
        session.options.dir = session.options.project + "/" + session.options.dir
    datafiles = []
    if session.options.download or session.options.recursive:
        response = requests.get(
            session.options.host
            + DOWNLOAD_FILE_URL
            + session.options.project
            + "/recursive",
            cookies=session.cookies,
            params={"cd": session.options.dir},
            verify=CA_BUNDLE,
        )
    elif session.options.download_all:
        response = requests.get(
            session.options.host
            + DOWNLOAD_FILE_URL
            + session.options.project
            + "/dirs",
            cookies=session.cookies,
            params={"cd": session.options.dir},
            verify=CA_BUNDLE,
        )
    else:
        sys.exit(1)

    if response.status_code != 200:
        print_error(response.text)
        sys.exit(1)
    datafiles = get_list(response.json(), session.options.output)
    if session.options.download:
        # Remove duplicates if present
        requested = list(set(_expand_requested(session, session.options.download)))
        allowed = _get_file_names(datafiles)

        datafiles = []
        for file in requested:
            file = f"{file}"
            if file not in allowed:
                print_warning(
                    f"WARNING: {file} is not a valid file for download, make sure the path is spelled correctly."
                )
                continue
            if file in allowed:
                print_file(file)
                datafiles.append(allowed[file])
        if not len(datafiles) > 0:
            print("No valid files to download")
            sys.exit(1)
        if input("Continuing on with the download of the existing files? (y/n)") != "y":
            sys.exit(1)

    if not os.path.isdir(
        session.options.output
    ):  # Create the output folder if it doesn't exist.
        os.makedirs(session.options.output)
    # Make sure directories exist
    datafiles = simplify_path(datafiles)
    make_directories(datafiles, output=session.options.output)
    get_url(session, datafiles)


def simplify_path(
    datafiles: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[str, int]]]:
    """Function to remove the project code from the project path. It is used to mimic the old gsport version file handling"""
    for file in datafiles:
        path = file["name"].split("/")
        subdirectories = path[1:]
        file["name"] = "/".join(subdirectories)
    return datafiles


def make_directories(
    files: List[Dict[str, Union[str, int]]],
    directory_path_length: int = 0,
    output: str = ".",
) -> None:
    """
        Create the directories that the files will be put in.
    :param files: The list of dictionaries containing file information.
    :param directory_path_length:
    :param output: The output directory.
    :return: None
    """
    for file in files:  # Go through every file.
        total_path = output  # Begin the path with the output directory.
        for path in file["name"].split("/")[
            directory_path_length:-1
        ]:  # Loop through the elements of the path, but not the file. This works because the server should never return "\" based paths.
            total_path = os.path.join(
                total_path, path
            )  # Append the path element to the total path.
            if not os.path.isdir(
                total_path
            ):  # Create the directory with the using the total path if it doesn't exist yet.
                try:
                    os.makedirs(total_path)
                except FileExistsError:
                    pass  # This can be the case with multithreading.
