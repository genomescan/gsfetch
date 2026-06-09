import os

GSFETCH_VERSION = "0.2.0"
CLIENT_VERSION = f"CLI_{GSFETCH_VERSION}"


ALL_PROJECTS_API = "api/projects"
LOGIN_URL = "login/"
LOGGED_IN_URL = "login/logged-in"
TWO_FACTOR_AUTH_URL = "login/two-factor"
LIST_RECURSIVE = "api/projects/"
LOGOUT_URL = "api/logout"
HOST_URL = os.getenv("HOST_URL", "https://dev.portal.genomescan.nl/")
VERIFY_FILES_URL = "api/downloads/"
DOWNLOAD_FILE_URL = "api/downloads/verify/"
CA_BUNDLE = True


LIST_EXAMPLE_MESSAGE = """
example usage:
  gsfetch list                                                   Show all projects currently available to you
  gsfetch list 100000                                            Show all project recursively
  gsfetch list 100000 -n                                         Show only file in the project root directory
  gsfetch list 100000 directory                                  Show all files inside directory recursively
  gsfetch list 100000 directory -n                               Show only the files in the directory, non recursively
  gsfetch list 100000 -md5                                       Show a list of md5 sum file pairs to allow for checking of correct file transfers
"""
DOWNLOAD_EXAMPLE_MESSAGE = """
example usage:
  gsfetch download 100000                                        Download all files of the project recursively
  gsfetch download 100000 -n                                     Downloads only file in the project root directory
  gsfetch download 100000 directory                              Downloads all files inside directory recursively
  gsfetch download 100000 directory -n                           Downloads only the files in the directory, non recursively
  gsfetch download 100000 -o output                              Downloads all files of the project to the folder named output
  gsfetch download 100000 file file                              Downloads all the files separated by spaces
  gsfetch download 100000 directory file                         Downloads directory recursively and specific file
"""
