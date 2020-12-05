#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-group.html
	get-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-group.html
	list-deployment-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-groups.html
	update-deployment-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html
    """

    write_parameter("deploy", "delete-deployment-group")