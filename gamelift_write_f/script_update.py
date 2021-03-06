#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-script : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-script.html
	delete-script : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-script.html
	describe-script : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-script.html
	list-scripts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-scripts.html
    """

    write_parameter("gamelift", "update-script")