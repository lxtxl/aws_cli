#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-human-task-ui : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-human-task-ui.html
	describe-human-task-ui : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-human-task-ui.html
	list-human-task-uis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-human-task-uis.html
    """

    write_parameter("sagemaker", "create-human-task-ui")