#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-matchmaking : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking.html
	stop-matchmaking : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-matchmaking.html
    """

    write_parameter("gamelift", "start-matchmaking")