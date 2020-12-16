#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-configurations.html
if __name__ == '__main__':
    """
	create-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-configuration.html
	delete-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/delete-configuration.html
	describe-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-configuration.html
	update-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("kafka", "list-configurations", add_option_dict)