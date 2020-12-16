#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-thing-registration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-registration-task.html
	list-thing-registration-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-registration-tasks.html
	start-thing-registration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-thing-registration-task.html
    """

    write_parameter("iot", "stop-thing-registration-task")