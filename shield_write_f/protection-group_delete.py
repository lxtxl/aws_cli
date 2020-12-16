#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection-group.html
	describe-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection-group.html
	list-protection-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protection-groups.html
	update-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/update-protection-group.html
    """

    write_parameter("shield", "delete-protection-group")