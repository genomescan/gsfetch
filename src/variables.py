import os

GSCLI_VERSION = "1.0"
CLIENT_VERSION = f"CLI_{GSCLI_VERSION}"


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
  gscli list 100000                                            Show all project recursively
  gscli list 100000 -n                                         Show only file in the project root directory
  gscli list 100000 directory                                  Show all files inside directory recursively
  gscli list 100000 -n directory                               Show only the files in the directory, non recursively
"""
DOWNLOAD_EXAMPLE_MESSAGE = """
example usage:
  gscli download 100000                                        Download all files of the project recursively
  gscli download 100000 -n                                     Downloads only file in the project root directory
  gscli download 100000 directory                              Downloads all files inside directory recursively
  gscli download 100000 -n directory                           Downloads only the files in the directory, non recursively
  gscli download 100000 -o output                              Downloads all files of the prohect to the folder named output
  gscli download 100000 file file                              Downloads all the files seperated by commas
  gscli download 100000 directory file                         Downloads directory recursively and specific file
"""
