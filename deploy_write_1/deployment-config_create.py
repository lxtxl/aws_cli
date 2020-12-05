#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-config.html
if __name__ == '__main__':
    """
	delete-deployment-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-config.html
	get-deployment-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-config.html
	list-deployment-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-configs.html
    """

    parameter_display_string = """
    # deployment-config-name : The name of the deployment configuration to create.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("deploy", "create-deployment-config", "deployment-config-name", add_option_dict)





