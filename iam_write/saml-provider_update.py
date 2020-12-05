#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-saml-provider.html
	delete-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-saml-provider.html
	get-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-saml-provider.html
	list-saml-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-saml-providers.html
    """

    write_parameter("iam", "update-saml-provider")