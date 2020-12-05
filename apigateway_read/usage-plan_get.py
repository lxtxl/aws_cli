#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plans.html
if __name__ == '__main__':
    """
	create-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan.html
	delete-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-usage-plan.html
	get-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan.html
	update-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-usage-plan.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("apigateway", "get-usage-plans", add_option_dict)