#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/initiate-document-version-upload.html
if __name__ == '__main__':
    """
	abort-document-version-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/abort-document-version-upload.html
    """

    parameter_display_string = """
    # parent-folder-id : The ID of the parent folder.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workdocs", "initiate-document-version-upload", "parent-folder-id", add_option_dict)





