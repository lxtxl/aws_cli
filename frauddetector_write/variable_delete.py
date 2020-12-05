#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-variable : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-variable.html
	get-variables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-variables.html
	update-variable : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-variable.html
    """

    write_parameter("frauddetector", "delete-variable")