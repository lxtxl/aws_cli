#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route.html
	delete-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route.html
	export-transit-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-transit-gateway-routes.html
	replace-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-transit-gateway-route.html
    """

    write_parameter("ec2", "search-transit-gateway-routes")