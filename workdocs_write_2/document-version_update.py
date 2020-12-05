#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document-version.html
if __name__ == '__main__':
    """
	describe-document-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-document-versions.html
	get-document-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document-version.html
    """

    parameter_display_string = """
    # document-id : The ID of the document.
    # version-id : The version ID of the document.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workdocs", "update-document-version", "document-id", "version-id", add_option_dict)
