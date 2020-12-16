#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-application.html
	describe-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-application.html
	list-simulation-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-applications.html
	update-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-simulation-application.html
    """

    write_parameter("robomaker", "delete-simulation-application")