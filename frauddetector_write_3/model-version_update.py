#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model-version.html
if __name__ == '__main__':
    """
	create-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model-version.html
	delete-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model-version.html
	describe-model-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html
	get-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html
    """

    parameter_display_string = """
    # model-id : The model ID.
    # model-type : The model type.
Possible values:

ONLINE_FRAUD_INSIGHTS
    # major-version-number : The major version number.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("frauddetector", "update-model-version", "model-id", "model-type", "major-version-number", add_option_dict)
