#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-traffic-policy-version.html
if __name__ == '__main__':
    """
	list-traffic-policy-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policy-versions.html
    """

    parameter_display_string = """
    # id : The ID of the traffic policy for which you want to create a new version.
    # document : The definition of this version of the traffic policy, in JSON format. You specified the JSON in the CreateTrafficPolicyVersion request. For more information about the JSON format, see CreateTrafficPolicy .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "create-traffic-policy-version", "id", "document", add_option_dict)
