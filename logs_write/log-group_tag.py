#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-log-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-group.html
	delete-log-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-group.html
	describe-log-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html
	untag-log-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/untag-log-group.html
    """

    write_parameter("logs", "tag-log-group")