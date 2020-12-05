#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-transit-gateway-routes.html
if __name__ == '__main__':
    """
	create-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route.html
	delete-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route.html
	export-transit-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-transit-gateway-routes.html
	replace-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-transit-gateway-route.html
    """

    parameter_display_string = """
    # transit-gateway-route-table-id : The ID of the transit gateway route table.
    # filters : One or more filters. The possible values are:

attachment.transit-gateway-attachment-id - The id of the transit gateway attachment.
attachment.resource-id - The resource id of the transit gateway attachment.
attachment.resource-type - The attachment resource type. Valid values are vpc | vpn | direct-connect-gateway | peering .
prefix-list-id - The ID of the prefix list.
route-search.exact-match - The exact match of the specified filter.
route-search.longest-prefix-match - The longest prefix that matches the route.
route-search.subnet-of-match - The routes with a subnet that match the specified CIDR filter.
route-search.supernet-of-match - The routes with a CIDR that encompass the CIDR filter. For example, if you have 10.0.1.0/29 and 10.0.1.0/31 routes in your route table and you specify supernet-of-match as 10.0.1.0/30, then the result returns 10.0.1.0/29.
state - The state of the route (active | blackhole ).
type - The type of route (propagated | static ).

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
    write_two_parameter("ec2", "search-transit-gateway-routes", "transit-gateway-route-table-id", "filters", add_option_dict)
