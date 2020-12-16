#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-predictor-backtest-export-job.html
if __name__ == '__main__':
    """
	create-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor-backtest-export-job.html
	describe-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-predictor-backtest-export-job.html
	list-predictor-backtest-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-predictor-backtest-export-jobs.html
    """

    parameter_display_string = """
    # predictor-backtest-export-job-arn : The Amazon Resource Name (ARN) of the predictor backtest export job to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("forecast", "delete-predictor-backtest-export-job", "predictor-backtest-export-job-arn", add_option_dict)





