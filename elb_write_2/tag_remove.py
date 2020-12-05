#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/remove-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/add-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-tags.html
    """

    parameter_display_string = """
    # load-balancer-names : The name of the load balancer. You can specify a maximum of one load balancer name.
(string)
    # tags : The list of tag keys to remove.
(structure)

The key of a tag.
Key -> (string)

The name of the key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "remove-tags", "load-balancer-names", "tags", add_option_dict)
