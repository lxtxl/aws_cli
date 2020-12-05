#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html
if __name__ == '__main__':
    """
	create-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html
	delete-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/delete-broker.html
	list-brokers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-brokers.html
	reboot-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/reboot-broker.html
	update-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/update-broker.html
    """

    parameter_display_string = """
    # broker-id : The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.
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

    execute_one_parameter("mq", "describe-broker", "broker-id", add_option_dict)