#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-predictor-backtest-export-job.html
if __name__ == '__main__':
    """
	create-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor-backtest-export-job.html
	delete-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-predictor-backtest-export-job.html
	list-predictor-backtest-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-predictor-backtest-export-jobs.html
    """

    parameter_display_string = """
    # predictor-backtest-export-job-arn : The Amazon Resource Name (ARN) of the predictor backtest export job.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("forecast", "describe-predictor-backtest-export-job", "predictor-backtest-export-job-arn", add_option_dict)