#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan-keys.html
if __name__ == '__main__':
    """
	create-usage-plan-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan-key.html
	delete-usage-plan-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-usage-plan-key.html
	get-usage-plan-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan-key.html
    """

    parameter_display_string = """
    # usage-plan-id : [Required] The Id of the  UsagePlan resource representing the usage plan containing the to-be-retrieved  UsagePlanKey resource representing a plan customer.
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

    execute_one_parameter("apigateway", "get-usage-plan-keys", "usage-plan-id", add_option_dict)