#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-alias.html
if __name__ == '__main__':
    """
	create-account-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-account-alias.html
    """

    parameter_display_string = """
    # account-alias : The name of the account alias to delete.
This parameter allows (through its regex pattern ) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-account-alias", "account-alias", add_option_dict)





