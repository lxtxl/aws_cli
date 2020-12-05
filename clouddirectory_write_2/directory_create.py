#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-directory.html
if __name__ == '__main__':
    """
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-directory.html
	disable-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/disable-directory.html
	enable-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/enable-directory.html
	get-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-directory.html
	list-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-directories.html
    """

    parameter_display_string = """
    # name : The name of the  Directory . Should be unique per account, per region.
    # schema-arn : The Amazon Resource Name (ARN) of the published schema that will be copied into the data  Directory . For more information, see  arns .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "create-directory", "name", "schema-arn", add_option_dict)
