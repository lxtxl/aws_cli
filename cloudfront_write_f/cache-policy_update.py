#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cache-policy.html
	delete-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-cache-policy.html
	get-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cache-policy.html
	list-cache-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cache-policies.html
    """

    write_parameter("cloudfront", "update-cache-policy")