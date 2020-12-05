#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/deregister-workspace-directory.html
if __name__ == '__main__':
    """
	describe-workspace-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-directories.html
	register-workspace-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/register-workspace-directory.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory. If any WorkSpaces are registered to this directory, you must remove them before you deregister the directory, or you will receive an OperationNotSupportedException error.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workspaces", "deregister-workspace-directory", "directory-id", add_option_dict)





