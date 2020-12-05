#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-peering-connection.html
	delete-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-peering-connection.html
	describe-vpc-peering-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-peering-connections.html
	reject-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-vpc-peering-connection.html
    """

    write_parameter("ec2", "accept-vpc-peering-connection")