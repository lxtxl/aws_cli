#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-configuration.html
if __name__ == '__main__':
    """
	delete-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/delete-configuration.html
	describe-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-configuration.html
	list-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-configurations.html
	update-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-configuration.html
    """

    parameter_display_string = """
    # name : The name of the configuration.
    # server-properties : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kafka", "create-configuration", "name", "server-properties", add_option_dict)
