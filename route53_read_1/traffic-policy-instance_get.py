#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-traffic-policy-instance.html
if __name__ == '__main__':
    """
	create-traffic-policy-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-traffic-policy-instance.html
	delete-traffic-policy-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-traffic-policy-instance.html
	list-traffic-policy-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policy-instances.html
	update-traffic-policy-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-traffic-policy-instance.html
    """

    parameter_display_string = """
    # id : The ID of the traffic policy instance that you want to get information about.
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

    execute_one_parameter("route53", "get-traffic-policy-instance", "id", add_option_dict)