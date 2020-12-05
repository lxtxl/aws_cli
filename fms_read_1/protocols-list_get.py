#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-protocols-list.html
if __name__ == '__main__':
    """
	delete-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-protocols-list.html
	list-protocols-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-protocols-lists.html
	put-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-protocols-list.html
    """

    parameter_display_string = """
    # list-id : The ID of the AWS Firewall Manager protocols list that you want the details for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("fms", "get-protocols-list", "list-id", add_option_dict)