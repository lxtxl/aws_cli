#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check.html
if __name__ == '__main__':
    """
	create-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-health-check.html
	delete-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-health-check.html
	list-health-checks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html
	update-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-health-check.html
    """

    parameter_display_string = """
    # health-check-id : The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
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

    execute_one_parameter("route53", "get-health-check", "health-check-id", add_option_dict)