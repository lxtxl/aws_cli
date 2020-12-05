#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-predictor.html
if __name__ == '__main__':
    """
	create-predictor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor.html
	delete-predictor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-predictor.html
	list-predictors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-predictors.html
    """

    parameter_display_string = """
    # predictor-arn : The Amazon Resource Name (ARN) of the predictor that you want information about.
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

    execute_one_parameter("forecast", "describe-predictor", "predictor-arn", add_option_dict)