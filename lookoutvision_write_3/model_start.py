#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-model.html
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-model.html
	describe-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html
	list-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-models.html
	stop-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/stop-model.html
    """

    parameter_display_string = """
    # project-name : The name of the project that contains the model that you want to start.
    # model-version : The version of the model that you want to start.
    # min-inference-units : The minimum number of inference units to use. A single inference unit represents 1 hour of processing and can support up to 5 Transaction Pers Second (TPS). Use a higher number to increase the TPS throughput of your model. You are charged for the number of inference units that you use.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lookoutvision", "start-model", "project-name", "model-version", "min-inference-units", add_option_dict)
