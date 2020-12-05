#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role.html
if __name__ == '__main__':
    """
	create-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html
	get-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role.html
	list-roles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-roles.html
	tag-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html
	untag-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html
	update-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role.html
    """

    parameter_display_string = """
    # role-name : The name of the role to delete.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-role", "role-name", add_option_dict)





