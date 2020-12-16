#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-ml-models.html
if __name__ == '__main__':
    """
	create-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-ml-model.html
	delete-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-ml-model.html
	get-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-ml-model.html
	update-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-ml-model.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("machinelearning", "describe-ml-models", add_option_dict)