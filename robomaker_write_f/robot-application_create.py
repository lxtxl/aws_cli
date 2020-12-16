#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot-application.html
	describe-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot-application.html
	list-robot-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robot-applications.html
	update-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-robot-application.html
    """

    write_parameter("robomaker", "create-robot-application")