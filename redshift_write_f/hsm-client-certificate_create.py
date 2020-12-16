#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-hsm-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-client-certificate.html
	describe-hsm-client-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-client-certificates.html
    """

    write_parameter("redshift", "create-hsm-client-certificate")