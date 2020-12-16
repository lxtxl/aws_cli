#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-traffic-policy-comment.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # id : The value of Id for the traffic policy that you want to update the comment for.
    # comment : The new comment for the specified traffic policy and version.
    # traffic-policy-version : The value of Version for the traffic policy that you want to update the comment for.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("route53", "update-traffic-policy-comment", "id", "comment", "traffic-policy-version", add_option_dict)
