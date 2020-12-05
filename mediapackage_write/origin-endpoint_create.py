#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/delete-origin-endpoint.html
	describe-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/describe-origin-endpoint.html
	list-origin-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-origin-endpoints.html
	update-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-origin-endpoint.html
    """

    write_parameter("mediapackage", "create-origin-endpoint")