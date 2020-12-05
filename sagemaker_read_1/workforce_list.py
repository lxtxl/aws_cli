#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-workforce.html
if __name__ == '__main__':
    """
	create-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workforce.html
	delete-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-workforce.html
	list-workforces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workforces.html
	update-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-workforce.html
    """

    parameter_display_string = """
    # workforce-name : The name of the private workforce whose access you want to restrict. WorkforceName is automatically set to default when a workforce is created and cannot be modified.
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

    execute_one_parameter("sagemaker", "describe-workforce", "workforce-name", add_option_dict)