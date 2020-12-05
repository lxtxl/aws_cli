#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-work-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html
	delete-work-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-work-group.html
	get-work-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-work-group.html
	list-work-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-work-groups.html
    """

    write_parameter("athena", "update-work-group")