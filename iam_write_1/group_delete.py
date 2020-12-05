#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-group.html
	get-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-groups.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-group.html
    """

    parameter_display_string = """
    # group-name : The name of the IAM group to delete.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-group", "group-name", add_option_dict)





