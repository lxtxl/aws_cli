#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	checkout-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/checkout-license.html
	create-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license.html
	get-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license.html
	list-licenses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-licenses.html
    """

    write_parameter("license-manager", "delete-license")