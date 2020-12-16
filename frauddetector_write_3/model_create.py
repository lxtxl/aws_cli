#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model.html
    """

    parameter_display_string = """
    # model-id : The model ID.
    # model-type : The model type.
Possible values:

ONLINE_FRAUD_INSIGHTS
    # event-type-name : The name of the event type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("frauddetector", "create-model", "model-id", "model-type", "event-type-name", add_option_dict)
