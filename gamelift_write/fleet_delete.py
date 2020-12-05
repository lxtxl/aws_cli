#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html
	list-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-fleets.html
    """

    write_parameter("gamelift", "delete-fleet")