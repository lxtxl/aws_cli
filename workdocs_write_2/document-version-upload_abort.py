#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/abort-document-version-upload.html
if __name__ == '__main__':
    """
	initiate-document-version-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/initiate-document-version-upload.html
    """

    parameter_display_string = """
    # document-id : The ID of the document.
    # version-id : The ID of the version.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workdocs", "abort-document-version-upload", "document-id", "version-id", add_option_dict)
