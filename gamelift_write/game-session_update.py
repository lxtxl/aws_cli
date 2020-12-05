#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-game-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session.html
	describe-game-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-sessions.html
	search-game-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/search-game-sessions.html
    """

    write_parameter("gamelift", "update-game-session")