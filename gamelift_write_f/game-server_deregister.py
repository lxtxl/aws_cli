#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	claim-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/claim-game-server.html
	describe-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server.html
	list-game-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-servers.html
	register-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-game-server.html
	update-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html
    """

    write_parameter("gamelift", "deregister-game-server")