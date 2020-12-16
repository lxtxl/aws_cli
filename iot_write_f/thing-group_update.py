#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-group.html
	delete-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-group.html
	describe-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-group.html
	list-thing-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-groups.html
    """

    write_parameter("iot", "update-thing-group")