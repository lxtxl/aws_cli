#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-identity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-identity-provider.html
	describe-identity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-identity-provider.html
	list-identity-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-identity-providers.html
	update-identity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-identity-provider.html
    """

    write_parameter("cognito-idp", "delete-identity-provider")