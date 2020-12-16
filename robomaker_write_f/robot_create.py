#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot.html
	deregister-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/deregister-robot.html
	describe-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot.html
	list-robots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robots.html
	register-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/register-robot.html
    """

    write_parameter("robomaker", "create-robot")