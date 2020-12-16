#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-forecast-export-job.html
if __name__ == '__main__':
    """
	delete-forecast-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-forecast-export-job.html
	describe-forecast-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-forecast-export-job.html
	list-forecast-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-forecast-export-jobs.html
    """

    parameter_display_string = """
    # forecast-export-job-name : The name for the forecast export job.
    # forecast-arn : The Amazon Resource Name (ARN) of the forecast that you want to export.
    # destination : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("forecast", "create-forecast-export-job", "forecast-export-job-name", "forecast-arn", "destination", add_option_dict)
