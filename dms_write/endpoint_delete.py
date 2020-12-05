#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html
	describe-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoints.html
	modify-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-endpoint.html
    """

    write_parameter("dms", "delete-endpoint")