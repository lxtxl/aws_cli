#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor-backtest-export-job.html
if __name__ == '__main__':
    """
	delete-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-predictor-backtest-export-job.html
	describe-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-predictor-backtest-export-job.html
	list-predictor-backtest-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-predictor-backtest-export-jobs.html
    """

    parameter_display_string = """
    # predictor-backtest-export-job-name : The name for the backtest export job.
    # predictor-arn : The Amazon Resource Name (ARN) of the predictor that you want to export.
    # destination : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("forecast", "create-predictor-backtest-export-job", "predictor-backtest-export-job-name", "predictor-arn", "destination", add_option_dict)
