#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-app-image-config.html
if __name__ == '__main__':
    """
	create-app-image-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app-image-config.html
	delete-app-image-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-app-image-config.html
	list-app-image-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-app-image-configs.html
	update-app-image-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-app-image-config.html
    """

    parameter_display_string = """
    # app-image-config-name : The name of the AppImageConfig to describe.
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

    execute_one_parameter("sagemaker", "describe-app-image-config", "app-image-config-name", add_option_dict)