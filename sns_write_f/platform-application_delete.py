#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-platform-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-platform-application.html
	list-platform-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-platform-applications.html
    """

    write_parameter("sns", "delete-platform-application")