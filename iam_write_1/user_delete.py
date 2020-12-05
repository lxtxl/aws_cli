#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html
	tag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html
	untag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html
    """

    parameter_display_string = """
    # user-name : The name of the user to delete.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-user", "user-name", add_option_dict)





