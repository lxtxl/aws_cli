#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-external-model.html
if __name__ == '__main__':
    """
	get-external-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-external-models.html
	put-external-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-external-model.html
    """

    parameter_display_string = """
    # model-endpoint : The endpoint of the Amazon Sagemaker model to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("frauddetector", "delete-external-model", "model-endpoint", add_option_dict)





