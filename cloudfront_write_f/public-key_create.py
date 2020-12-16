#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-public-key.html
	get-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-public-key.html
	list-public-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-public-keys.html
	update-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-public-key.html
    """

    write_parameter("cloudfront", "create-public-key")