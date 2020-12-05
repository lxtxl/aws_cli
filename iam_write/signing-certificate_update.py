#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html
	list-signing-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html
	upload-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html
    """

    write_parameter("iam", "update-signing-certificate")