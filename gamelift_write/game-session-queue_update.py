#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session-queue.html
	delete-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-game-session-queue.html
	describe-game-session-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-session-queues.html
    """

    write_parameter("gamelift", "update-game-session-queue")