#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-origin-request-policy.html
	delete-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-origin-request-policy.html
	get-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-origin-request-policy.html
	list-origin-request-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-origin-request-policies.html
    """

    write_parameter("cloudfront", "update-origin-request-policy")