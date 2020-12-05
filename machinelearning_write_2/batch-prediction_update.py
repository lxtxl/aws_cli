#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-batch-prediction.html
if __name__ == '__main__':
    """
	create-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-batch-prediction.html
	delete-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-batch-prediction.html
	describe-batch-predictions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-batch-predictions.html
	get-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-batch-prediction.html
    """

    parameter_display_string = """
    # batch-prediction-id : The ID assigned to the BatchPrediction during creation.
    # batch-prediction-name : A new user-supplied name or description of the BatchPrediction .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("machinelearning", "update-batch-prediction", "batch-prediction-id", "batch-prediction-name", add_option_dict)
