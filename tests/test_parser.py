import sys
import unittest
from unittest.mock import patch

from src.classes import Options

"""
Tests for the argument parser in the Options class.

Each test checks that specific command-line arguments are correctly
parsed and assign the appropriate attributes.

Author: Gonzalo Vela
"""


class TestArgumentParser(unittest.TestCase):
    @patch("sys.argv", ["script_name", "-H", "test_host"])
    def test_host(self):
        """
        Test of host argument
        """
        options = Options(sys.argv)
        assert options.host == "test_host"

    @patch("sys.argv", ["script_name", "-c"])
    def test_clear_cookies(self):
        """
        Test of clear cookies flag
        """
        options = Options(sys.argv)
        assert options.clear_cookies

    @patch("sys.argv", ["script_name", "list", "999", "test_dir"])
    def test_set_directory(self):
        """
        Test of custom directory argument
        """
        options = Options(sys.argv)
        assert options.dir == "test_dir/"

    @patch("sys.argv", ["script_name", "list", "999"])
    def test_set_recursive(self):
        """
        Test of recursive flag
        """
        options = Options(sys.argv)
        assert options.recursive

    @patch("sys.argv", ["script_name", "list", "999", "-n"])
    def test_set_non_recursive(self):
        """
        Test of recursive flag
        """
        options = Options(sys.argv)
        assert not options.recursive

    @patch("sys.argv", ["script_name", "list", "999", "test_dir"])
    def test_set_recursive_directory(self):
        """
        Test of recursive flag with custom directory
        """
        options = Options(sys.argv)
        assert options.recursive
        assert options.dir == "test_dir/"

    @patch("sys.argv", ["script_name", "list", "-n", "999", "test_dir"])
    def test_set_non_recursive_directory(self):
        """
        Test of recursive flag with custom directory
        """
        options = Options(sys.argv)
        assert not options.recursive
        assert options.dir == "test_dir/"

    @patch("sys.argv", ["script_name", "download", "999", "-o", "test_dir"])
    def test_set_output(self):
        """
        Test of output directory argument
        """
        options = Options(sys.argv)
        assert options.output == "test_dir"

    @patch("sys.argv", ["script_name", "download", "999", "-t", "4"])
    def test_set_threads(self):
        """
        Test of thread count argument
        """
        options = Options(sys.argv)
        assert options.threads == 4

    @patch("sys.argv", ["script_name", "download", "999"])
    def test_set_recursive_download(self):
        """
        Test of recursive download flag
        """
        options = Options(sys.argv)
        assert options.recursive

    @patch("sys.argv", ["script_name", "download", "999", "-n"])
    def test_set_non_recursive_download(self):
        """
        Test of non recursive download flag
        """
        options = Options(sys.argv)
        assert not options.recursive
