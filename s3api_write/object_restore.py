#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	copy-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html
	delete-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html
	delete-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html
	get-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html
	head-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html
	list-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html
	put-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html
    """

    write_parameter("s3api", "restore-object")