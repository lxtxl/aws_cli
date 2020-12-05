#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/disable-directory.html
if __name__ == '__main__':
    """
	create-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-directory.html
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-directory.html
	enable-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/enable-directory.html
	get-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-directory.html
	list-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-directories.html
    """

    parameter_display_string = """
    # directory-arn : The ARN of the directory to disable.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("clouddirectory", "disable-directory", "directory-arn", add_option_dict)





