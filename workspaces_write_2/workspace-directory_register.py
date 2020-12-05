#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/register-workspace-directory.html
if __name__ == '__main__':
    """
	deregister-workspace-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/deregister-workspace-directory.html
	describe-workspace-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-directories.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory. You cannot register a directory if it does not have a status of Active. If the directory does not have a status of Active, you will receive an InvalidResourceStateException error. If you have already registered the maximum number of directories that you can register with Amazon WorkSpaces, you will receive a ResourceLimitExceededException error. Deregister directories that you are not using for WorkSpaces, and try again.
    # enable-work-docs | --no-enable-work-docs : Indicates whether Amazon WorkDocs is enabled or disabled. If you have enabled this parameter and WorkDocs is not available in the Region, you will receive an OperationNotSupportedException error. Set EnableWorkDocs to disabled, and try again.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "register-workspace-directory", "directory-id", "enable-work-docs | --no-enable-work-docs", add_option_dict)
