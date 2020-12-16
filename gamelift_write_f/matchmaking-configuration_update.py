#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-matchmaking-configuration.html
	delete-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-matchmaking-configuration.html
	describe-matchmaking-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking-configurations.html
    """

    write_parameter("gamelift", "update-matchmaking-configuration")