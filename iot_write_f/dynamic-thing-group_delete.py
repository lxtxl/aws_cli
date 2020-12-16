#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-dynamic-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-dynamic-thing-group.html
	update-dynamic-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dynamic-thing-group.html
    """

    write_parameter("iot", "delete-dynamic-thing-group")