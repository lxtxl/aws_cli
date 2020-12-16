#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-signing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/cancel-signing-profile.html
	get-signing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-signing-profile.html
	list-signing-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-profiles.html
	revoke-signing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/revoke-signing-profile.html
    """

    write_parameter("signer", "put-signing-profile")