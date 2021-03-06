#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule-destination.html
if __name__ == '__main__':
    """
	confirm-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/confirm-topic-rule-destination.html
	create-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule-destination.html
	delete-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule-destination.html
	list-topic-rule-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rule-destinations.html
	update-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-topic-rule-destination.html
    """

    parameter_display_string = """
    # arn : The ARN of the topic rule destination.
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

    execute_one_parameter("iot", "get-topic-rule-destination", "arn", add_option_dict)