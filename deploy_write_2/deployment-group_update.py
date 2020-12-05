#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html
if __name__ == '__main__':
    """
	create-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-group.html
	delete-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-group.html
	get-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-group.html
	list-deployment-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-groups.html
    """

    parameter_display_string = """
    # application-name : The application name that corresponds to the deployment group to update.
    # current-deployment-group-name : The current name of the deployment group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("deploy", "update-deployment-group", "application-name", "current-deployment-group-name", add_option_dict)
