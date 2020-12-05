#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployments.html
if __name__ == '__main__':
    """
	continue-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/continue-deployment.html
	create-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html
	get-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment.html
	stop-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/stop-deployment.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("deploy", "list-deployments", add_option_dict)