#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html
if __name__ == '__main__':
    """
	create-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model-version.html
	delete-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model-version.html
	describe-model-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html
	update-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model-version.html
    """

    parameter_display_string = """
    # model-id : The model ID.
    # model-type : The model type.
Possible values:

ONLINE_FRAUD_INSIGHTS
    """

    execute_two_parameter("frauddetector", "get-model-version", "model-id", "model-type", parameter_display_string)