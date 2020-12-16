#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-user-hierarchy-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user-hierarchy-group.html
	describe-user-hierarchy-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user-hierarchy-group.html
	list-user-hierarchy-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-user-hierarchy-groups.html
    """

    write_parameter("connect", "delete-user-hierarchy-group")