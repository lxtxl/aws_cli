#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates.html
	register-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-certificate.html
	transfer-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/transfer-certificate.html
	update-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html
    """

    write_parameter("iot", "delete-certificate")