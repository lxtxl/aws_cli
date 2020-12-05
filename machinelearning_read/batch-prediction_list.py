#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-batch-predictions.html
if __name__ == '__main__':
    """
	create-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-batch-prediction.html
	delete-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-batch-prediction.html
	get-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-batch-prediction.html
	update-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-batch-prediction.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("machinelearning", "describe-batch-predictions", add_option_dict)