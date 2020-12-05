#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/select-aggregate-resource-config.html
if __name__ == '__main__':
    """
	get-aggregate-resource-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-resource-config.html
    """

    parameter_display_string = """
    # expression : The SQL query SELECT command.
    # configuration-aggregator-name : The name of the configuration aggregator.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "select-aggregate-resource-config", "expression", "configuration-aggregator-name", add_option_dict)
