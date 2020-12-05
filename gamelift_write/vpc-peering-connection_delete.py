#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-vpc-peering-connection.html
	describe-vpc-peering-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-vpc-peering-connections.html
    """

    write_parameter("gamelift", "delete-vpc-peering-connection")