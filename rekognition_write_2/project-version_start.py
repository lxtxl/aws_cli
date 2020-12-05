#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-project-version.html
if __name__ == '__main__':
    """
	create-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project-version.html
	delete-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-project-version.html
	describe-project-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-project-versions.html
	stop-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-project-version.html
    """

    parameter_display_string = """
    # project-version-arn : The Amazon Resource Name(ARN) of the model version that you want to start.
    # min-inference-units : The minimum number of inference units to use. A single inference unit represents 1 hour of processing and can support up to 5 Transaction Pers Second (TPS). Use a higher number to increase the TPS throughput of your model. You are charged for the number of inference units that you use.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rekognition", "start-project-version", "project-version-arn", "min-inference-units", add_option_dict)
