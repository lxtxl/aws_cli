#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-notebook-instances.html
if __name__ == '__main__':
    """
	create-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance.html
	delete-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-notebook-instance.html
	describe-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-notebook-instance.html
	start-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-notebook-instance.html
	stop-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-notebook-instance.html
	update-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("sagemaker", "list-notebook-instances", add_option_dict)