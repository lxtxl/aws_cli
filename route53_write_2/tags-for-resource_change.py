#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-tags-for-resource.html
if __name__ == '__main__':
    """
	list-tags-for-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-tags-for-resource.html
	list-tags-for-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-tags-for-resources.html
    """

    parameter_display_string = """
    # resource-type : The type of the resource.

The resource type for health checks is healthcheck .
The resource type for hosted zones is hostedzone .

Possible values:

healthcheck
hostedzone
    # resource-id : The ID of the resource for which you want to add, change, or delete tags.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "change-tags-for-resource", "resource-type", "resource-id", add_option_dict)
