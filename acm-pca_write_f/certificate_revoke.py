#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html
	issue-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html
    """

    write_parameter("acm-pca", "revoke-certificate")