#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-groups.html
if __name__ == '__main__':
    """
	create-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-group.html
	delete-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-group.html
	get-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-group.html
	update-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html
    """

    parameter_display_string = """
    # application-name : The name of an AWS CodeDeploy application associated with the IAM user or AWS account.
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

    execute_one_parameter("deploy", "list-deployment-groups", "application-name", add_option_dict)