#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment.html
	describe-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-environments.html
    """

    write_parameter("cloud9", "update-environment")