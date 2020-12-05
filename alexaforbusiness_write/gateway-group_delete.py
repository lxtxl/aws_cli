#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-gateway-group.html
	get-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-gateway-group.html
	list-gateway-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-gateway-groups.html
	update-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-gateway-group.html
    """

    write_parameter("alexaforbusiness", "delete-gateway-group")