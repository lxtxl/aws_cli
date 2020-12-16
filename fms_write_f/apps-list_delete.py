#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-apps-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-apps-list.html
	list-apps-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-apps-lists.html
	put-apps-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-apps-list.html
    """

    write_parameter("fms", "delete-apps-list")