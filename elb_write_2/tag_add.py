#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/add-tags.html
if __name__ == '__main__':
    """
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-tags.html
	remove-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/remove-tags.html
    """

    parameter_display_string = """
    # load-balancer-names : The name of the load balancer. You can specify one load balancer only.
(string)
    # tags : The tags.
(structure)

Information about a tag.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "add-tags", "load-balancer-names", "tags", add_option_dict)
