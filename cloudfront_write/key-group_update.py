#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-key-group.html
	delete-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-key-group.html
	get-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-key-group.html
	list-key-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-key-groups.html
    """

    write_parameter("cloudfront", "update-key-group")