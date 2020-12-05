#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-identity-policy.html
	get-email-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-identity-policies.html
	update-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-email-identity-policy.html
    """

    write_parameter("sesv2", "delete-email-identity-policy")