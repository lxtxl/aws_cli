#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-local-gateway-routes.html
if __name__ == '__main__':
    """
	create-local-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route.html
	delete-local-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-local-gateway-route.html
    """

    parameter_display_string = """
    # local-gateway-route-table-id : The ID of the local gateway route table.
    # filters : One or more filters.
(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:

DescribeAvailabilityZones
DescribeImages
DescribeInstances
DescribeKeyPairs
DescribeSecurityGroups
DescribeSnapshots
DescribeSubnets
DescribeTags
DescribeVolumes
DescribeVpcs

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "search-local-gateway-routes", "local-gateway-route-table-id", "filters", add_option_dict)
