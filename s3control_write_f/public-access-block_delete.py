#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-public-access-block.html
	put-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-public-access-block.html
    """

    write_parameter("s3control", "delete-public-access-block")