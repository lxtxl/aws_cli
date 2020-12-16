#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-server-certificate.html
	get-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-server-certificate.html
	list-server-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-server-certificates.html
	upload-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-server-certificate.html
    """

    write_parameter("iam", "update-server-certificate")