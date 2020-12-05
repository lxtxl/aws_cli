#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-predictor.html
if __name__ == '__main__':
    """
	create-predictor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor.html
	describe-predictor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-predictor.html
	list-predictors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-predictors.html
    """

    parameter_display_string = """
    # predictor-arn : The Amazon Resource Name (ARN) of the predictor to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("forecast", "delete-predictor", "predictor-arn", add_option_dict)





