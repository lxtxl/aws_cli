#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-certificates.html
    """

    write_parameter("ds", "register-certificate")