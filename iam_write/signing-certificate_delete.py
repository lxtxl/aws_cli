#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-signing-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html
	update-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html
	upload-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html
    """

    write_parameter("iam", "delete-signing-certificate")