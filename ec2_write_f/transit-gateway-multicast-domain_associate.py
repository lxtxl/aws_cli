#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-transit-gateway-multicast-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-multicast-domain.html
	delete-transit-gateway-multicast-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-multicast-domain.html
	describe-transit-gateway-multicast-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-multicast-domains.html
	disassociate-transit-gateway-multicast-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-transit-gateway-multicast-domain.html
    """

    write_parameter("ec2", "associate-transit-gateway-multicast-domain")