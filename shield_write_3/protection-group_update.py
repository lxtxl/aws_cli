#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/update-protection-group.html
if __name__ == '__main__':
    """
	create-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection-group.html
	delete-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/delete-protection-group.html
	describe-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection-group.html
	list-protection-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protection-groups.html
    """

    parameter_display_string = """
    # protection-group-id : The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
    # aggregation : Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.

Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
Max - Use the highest traffic from each resource. This is useful for resources that donât share traffic and for resources that share that traffic in a non-uniform way. Examples include CloudFront distributions and origin resources for CloudFront distributions.

Possible values:

SUM
MEAN
MAX
    # pattern : The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
Possible values:

ALL
ARBITRARY
BY_RESOURCE_TYPE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("shield", "update-protection-group", "protection-group-id", "aggregation", "pattern", add_option_dict)
