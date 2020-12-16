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
	update-game-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session.html
    """

    write_parameter("gamelift", "search-game-sessions")