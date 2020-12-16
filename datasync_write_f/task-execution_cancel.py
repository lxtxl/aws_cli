#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task-execution.html
	list-task-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-task-executions.html
	start-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/start-task-execution.html
	update-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task-execution.html
    """

    write_parameter("datasync", "cancel-task-execution")