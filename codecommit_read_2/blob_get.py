#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-blob.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The name of the repository that contains the blob.
    # blob-id : The ID of the blob, which is its SHA-1 pointer.
    """

    execute_two_parameter("codecommit", "get-blob", "repository-name", "blob-id", parameter_display_string)