#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-input-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-input-security-group.html
	delete-input-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-input-security-group.html
	describe-input-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input-security-group.html
	list-input-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-security-groups.html
    """

    write_parameter("medialive", "update-input-security-group")