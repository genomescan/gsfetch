from typing import Dict


def is_file(file: Dict | str) -> bool:
    """
        Check if a row entry is a file. Serves as substitute for the type field removal in the new customer portal
    :param session: Session object.
    :return: None
    """
    if isinstance(file, Dict):
        return file["size"] is not None
    print(file)
    return False if "." not in file else True
