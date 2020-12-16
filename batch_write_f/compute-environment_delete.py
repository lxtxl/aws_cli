#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html
	describe-compute-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-compute-environments.html
	update-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html
    """

    write_parameter("batch", "delete-compute-environment")