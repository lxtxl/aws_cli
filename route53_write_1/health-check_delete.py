#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-health-check.html
if __name__ == '__main__':
    """
	create-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-health-check.html
	get-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check.html
	list-health-checks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html
	update-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-health-check.html
    """

    parameter_display_string = """
    # health-check-id : The ID of the health check that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53", "delete-health-check", "health-check-id", add_option_dict)





