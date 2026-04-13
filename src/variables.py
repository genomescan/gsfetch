from pathlib import Path

GSCLI_VERSION = "1.0"
CLIENT_VERSION = f"CLI_{GSCLI_VERSION}"


ROOT_DIR = Path(__file__).parent.parent
ALL_PROJECTS_API = "api/projects"
LOGIN_URL = "login/"
LOGGED_IN_URL = "login/logged-in"
TWO_FACTOR_AUTH_URL = "login/two-factor"
LIST_RECURSIVE = "api/projects/"
DOWNLOAD_RECURSIVE = "/data_api_recursive/"
LOGOUT_URL = "api/logout"
# HOST_URL = "https://10.159.5.194/"
HOST_URL = "http://127.0.0.1:8000/"
VERIFY_FILES_URL = "api/downloads/"
DOWNLOAD_FILE_URL = "api/downloads/verify/"
CA_BUNDLE = False


LIST_EXAMPLE_MESSAGE = """
example usage:
  gsport list 100000                                            Show all project recursively
  gsport list 100000 -n                                         Show only file in the project root directory
  gsport list 100000 directory                                  Show all files inside directory recursively
  gsport list 100000 -n directory                               Show only the files in the directory, non recursively
"""
DOWNLOAD_EXAMPLE_MESSAGE = """
example usage:
  gsport download 100000                                        Download all project recursively
  gsport download 100000 -n                                     Downloads only file in the project root directory
  gsport download 100000 directory                              Downloads all files inside directory recursively
  gsport download 100000 -n directory                           Downloads only the files in the directory, non recursively
  gsport download 100000 -o output                              Downloads files to folder output
  gsport download 100000 file, file                             Downloads list of files
  gsport download 100000 directory, file                        Downloads directory recursively and specific file
"""
