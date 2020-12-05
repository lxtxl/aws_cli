#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-batch-prediction.html
if __name__ == '__main__':
    """
	create-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-batch-prediction.html
	delete-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-batch-prediction.html
	describe-batch-predictions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-batch-predictions.html
	update-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-batch-prediction.html
    """

    parameter_display_string = """
    # batch-prediction-id : An ID assigned to the BatchPrediction at creation.
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

    execute_one_parameter("machinelearning", "get-batch-prediction", "batch-prediction-id", add_option_dict)