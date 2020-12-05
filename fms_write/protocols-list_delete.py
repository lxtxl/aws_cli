#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-protocols-list.html
	list-protocols-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-protocols-lists.html
	put-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-protocols-list.html
    """

    write_parameter("fms", "delete-protocols-list")