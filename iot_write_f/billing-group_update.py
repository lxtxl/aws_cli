#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-billing-group.html
	delete-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-billing-group.html
	describe-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-billing-group.html
	list-billing-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-billing-groups.html
    """

    write_parameter("iot", "update-billing-group")