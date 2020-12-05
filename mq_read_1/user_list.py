#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-users.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/delete-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/update-user.html
    """

    parameter_display_string = """
    # broker-id : The unique ID that Amazon MQ generates for the broker.
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

    execute_one_parameter("mq", "list-users", "broker-id", add_option_dict)