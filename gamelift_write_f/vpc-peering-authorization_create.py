#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-vpc-peering-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-vpc-peering-authorization.html
	describe-vpc-peering-authorizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-vpc-peering-authorizations.html
    """

    write_parameter("gamelift", "create-vpc-peering-authorization")