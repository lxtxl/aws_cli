#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-deployment.html
if __name__ == '__main__':
    """
	list-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-deployments.html
	reset-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/reset-deployments.html
    """

    parameter_display_string = """
    # deployment-type : Possible values:

NewDeployment
Redeployment
ResetDeployment
ForceResetDeployment
    # group-id : The ID of the Greengrass group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("greengrass", "create-deployment", "deployment-type", "group-id", add_option_dict)
