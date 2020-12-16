#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identities.html
	describe-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity.html
	list-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identities.html
    """

    write_parameter("cognito-identity", "unlink-identity")