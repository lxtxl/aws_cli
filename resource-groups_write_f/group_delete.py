#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html
	get-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-groups.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group.html
    """

    write_parameter("resource-groups", "delete-group")