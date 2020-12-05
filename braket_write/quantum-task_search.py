#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/cancel-quantum-task.html
	create-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/create-quantum-task.html
	get-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-quantum-task.html
    """

    write_parameter("braket", "search-quantum-tasks")