#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-usage.html
if __name__ == '__main__':
    """
	get-usage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage.html
    """

    parameter_display_string = """
    # usage-plan-id : [Required] The Id of the usage plan associated with the usage data.
    # key-id : [Required] The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "update-usage", "usage-plan-id", "key-id", add_option_dict)
