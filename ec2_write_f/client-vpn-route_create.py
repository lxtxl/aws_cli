#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-client-vpn-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-client-vpn-route.html
	describe-client-vpn-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-routes.html
    """

    write_parameter("ec2", "create-client-vpn-route")