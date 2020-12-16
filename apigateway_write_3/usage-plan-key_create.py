#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan-key.html
if __name__ == '__main__':
    """
	delete-usage-plan-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-usage-plan-key.html
	get-usage-plan-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan-key.html
	get-usage-plan-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan-keys.html
    """

    parameter_display_string = """
    # usage-plan-id : [Required] The Id of the  UsagePlan resource representing the usage plan containing the to-be-created  UsagePlanKey resource representing a plan customer.
    # key-id : [Required] The identifier of a  UsagePlanKey resource for a plan customer.
    # key-type : [Required] The type of a  UsagePlanKey resource for a plan customer.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigateway", "create-usage-plan-key", "usage-plan-id", "key-id", "key-type", add_option_dict)
