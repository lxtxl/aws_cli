#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	accept-transit-gateway-peering-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-transit-gateway-peering-attachment.html
	create-transit-gateway-peering-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-peering-attachment.html
	delete-transit-gateway-peering-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-peering-attachment.html
	describe-transit-gateway-peering-attachments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-peering-attachments.html
    """

    write_parameter("ec2", "reject-transit-gateway-peering-attachment")