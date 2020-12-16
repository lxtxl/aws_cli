#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/create-environment.html
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/delete-environment.html
	get-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/get-environment.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/list-environments.html
    """

    write_parameter("mwaa", "update-environment")