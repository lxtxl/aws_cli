#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-configuration.html
if __name__ == '__main__':
    """
	create-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-configuration.html
	delete-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/delete-configuration.html
	describe-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-configuration.html
	list-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-configurations.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the configuration.
    # server-properties : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kafka", "update-configuration", "arn", "server-properties", add_option_dict)
