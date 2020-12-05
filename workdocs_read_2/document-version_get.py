#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document-version.html
if __name__ == '__main__':
    """
	describe-document-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-document-versions.html
	update-document-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document-version.html
    """

    parameter_display_string = """
    # document-id : The ID of the document.
    # version-id : The version ID of the document.
    """

    execute_two_parameter("workdocs", "get-document-version", "document-id", "version-id", parameter_display_string)