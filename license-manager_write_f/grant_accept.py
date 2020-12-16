#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-grant.html
	delete-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-grant.html
	get-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-grant.html
	reject-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/reject-grant.html
    """

    write_parameter("license-manager", "accept-grant")