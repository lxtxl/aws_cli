#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-vpc-association-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-vpc-association-authorization.html
	list-vpc-association-authorizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-vpc-association-authorizations.html
    """

    write_parameter("route53", "create-vpc-association-authorization")