#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-notebook-instance-lifecycle-config.html
if __name__ == '__main__':
    """
	create-notebook-instance-lifecycle-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance-lifecycle-config.html
	delete-notebook-instance-lifecycle-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-notebook-instance-lifecycle-config.html
	list-notebook-instance-lifecycle-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-notebook-instance-lifecycle-configs.html
	update-notebook-instance-lifecycle-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance-lifecycle-config.html
    """

    parameter_display_string = """
    # notebook-instance-lifecycle-config-name : The name of the lifecycle configuration to describe.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("sagemaker", "describe-notebook-instance-lifecycle-config", "notebook-instance-lifecycle-config-name", add_option_dict)