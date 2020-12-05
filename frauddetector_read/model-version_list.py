#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html
if __name__ == '__main__':
    """
	create-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model-version.html
	delete-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model-version.html
	get-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html
	update-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model-version.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("frauddetector", "describe-model-versions", add_option_dict)