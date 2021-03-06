#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-account.html
if __name__ == '__main__':
    """
	create-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-account.html
	get-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-accounts.html
	update-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-account.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "delete-account", "account-id", add_option_dict)





