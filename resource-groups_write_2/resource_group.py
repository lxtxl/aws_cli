#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/group-resources.html
if __name__ == '__main__':
    """
	search-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html
	ungroup-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/ungroup-resources.html
    """

    parameter_display_string = """
    # group : The name or the ARN of the resource group to add resources to.
    # resource-arns : The list of ARNs for resources to be added to the group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("resource-groups", "group-resources", "group", "resource-arns", add_option_dict)
