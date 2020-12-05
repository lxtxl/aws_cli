#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-ca-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-ca-certificate.html
	describe-ca-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html
	list-ca-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-ca-certificates.html
	update-ca-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html
    """

    write_parameter("iot", "register-ca-certificate")