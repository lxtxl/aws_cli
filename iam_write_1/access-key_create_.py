#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html
if __name__ == '__main__':
    """
	create-access-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-access-key.html
	list-access-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html
	update-access-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-access-key.html
    """

    parameter_display_string = """
    # access-key-id : The access key ID for the access key ID and secret access key you want to delete.
This parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "create-access-key", "user-name", add_option_dict)





