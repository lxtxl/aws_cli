#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/detach-object.html
if __name__ == '__main__':
    """
	attach-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/attach-object.html
	create-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-object.html
	delete-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-object.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory where objects reside. For more information, see  arns .
    # parent-reference : 
    # link-name : The link name associated with the object that needs to be detached.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("clouddirectory", "detach-object", "directory-arn", "parent-reference", "link-name", add_option_dict)
