#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-email-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-email-identity.html
	get-email-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-email-identity.html
	list-email-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-email-identities.html
    """

    write_parameter("pinpoint-email", "delete-email-identity")