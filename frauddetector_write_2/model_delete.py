#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model.html
    """

    parameter_display_string = """
    # model-id : The model ID of the model to delete.
    # model-type : The model type of the model to delete.
Possible values:

ONLINE_FRAUD_INSIGHTS
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("frauddetector", "delete-model", "model-id", "model-type", add_option_dict)
