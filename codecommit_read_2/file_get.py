#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-file.html
if __name__ == '__main__':
    """
	delete-file : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-file.html
	put-file : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-file.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository that contains the file.
    # file-path : The fully qualified path to the file, including the full name and extension of the file. For example, /examples/file.md is the fully qualified path to a file named file.md in a folder named examples.
    """

    execute_two_parameter("codecommit", "get-file", "repository-name", "file-path", parameter_display_string)