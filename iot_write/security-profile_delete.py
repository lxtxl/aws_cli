#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-security-profile.html
	create-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html
	describe-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-security-profile.html
	detach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-security-profile.html
	list-security-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-security-profiles.html
	update-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-security-profile.html
    """

    write_parameter("iot", "delete-security-profile")