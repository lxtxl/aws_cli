#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-tagging.html
	get-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html
    """

    write_parameter("s3api", "put-bucket-tagging")