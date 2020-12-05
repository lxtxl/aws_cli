#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-ml-model.html
if __name__ == '__main__':
    """
	create-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-ml-model.html
	delete-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-ml-model.html
	describe-ml-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-ml-models.html
	get-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-ml-model.html
    """

    parameter_display_string = """
    # ml-model-id : The ID assigned to the MLModel during creation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("machinelearning", "update-ml-model", "ml-model-id", add_option_dict)





