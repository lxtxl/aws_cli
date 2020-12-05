#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html
	list-service-specific-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html
	reset-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html
	update-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html
    """

    write_parameter("iam", "create-service-specific-credential")