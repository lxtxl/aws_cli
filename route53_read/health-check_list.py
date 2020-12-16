#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html
if __name__ == '__main__':
    """
	create-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-health-check.html
	delete-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-health-check.html
	get-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check.html
	update-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-health-check.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("route53", "list-health-checks", add_option_dict)