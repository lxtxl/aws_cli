#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-traffic-policy.html
if __name__ == '__main__':
    """
	delete-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-traffic-policy.html
	get-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-traffic-policy.html
	list-traffic-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policies.html
    """

    parameter_display_string = """
    # name : The name of the traffic policy.
    # document : The definition of this traffic policy in JSON format. For more information, see Traffic Policy Document Format .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "create-traffic-policy", "name", "document", add_option_dict)
