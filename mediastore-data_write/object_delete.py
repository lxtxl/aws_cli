#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/describe-object.html
	get-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/get-object.html
	put-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/put-object.html
    """

    write_parameter("mediastore-data", "delete-object")