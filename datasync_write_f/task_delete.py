#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html
	describe-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-tasks.html
	update-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task.html
    """

    write_parameter("datasync", "delete-task")