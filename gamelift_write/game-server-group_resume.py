#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-server-group.html
	delete-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-game-server-group.html
	describe-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server-group.html
	list-game-server-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-server-groups.html
	suspend-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/suspend-game-server-group.html
	update-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server-group.html
    """

    write_parameter("gamelift", "resume-game-server-group")