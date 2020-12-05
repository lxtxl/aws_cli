#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecastquery/query-forecast.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # forecast-arn : The Amazon Resource Name (ARN) of the forecast to query.
    # filters : The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for client_21 in the electricity usage dataset, specify the following:

{"item_id" : "client_21"}

To get the full forecast, use the CreateForecastExportJob operation.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("forecastquery", "query-forecast", "forecast-arn", "filters", add_option_dict)
