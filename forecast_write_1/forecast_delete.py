#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-forecast.html
if __name__ == '__main__':
    """
	create-forecast : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-forecast.html
	describe-forecast : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-forecast.html
	list-forecasts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-forecasts.html
    """

    parameter_display_string = """
    # forecast-arn : The Amazon Resource Name (ARN) of the forecast to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("forecast", "delete-forecast", "forecast-arn", add_option_dict)





