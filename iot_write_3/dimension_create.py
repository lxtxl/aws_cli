#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-dimension.html
if __name__ == '__main__':
    """
	delete-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-dimension.html
	describe-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-dimension.html
	list-dimensions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-dimensions.html
	update-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dimension.html
    """

    parameter_display_string = """
    # name : A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.
    # type : Specifies the type of dimension. Supported types: TOPIC_FILTER.
Possible values:

TOPIC_FILTER
    # string-values : Specifies the value or list of values for the dimension. For TOPIC_FILTER dimensions, this is a pattern used to match the MQTT topic (for example, âadmin/#â).
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "create-dimension", "name", "type", "string-values", add_option_dict)
