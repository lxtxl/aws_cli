#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution.html
	delete-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution.html
	get-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution.html
	list-distributions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distributions.html
    """

    write_parameter("cloudfront", "update-distribution")