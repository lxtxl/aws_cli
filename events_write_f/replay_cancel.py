#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-replay : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-replay.html
	list-replays : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-replays.html
	start-replay : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/start-replay.html
    """

    write_parameter("events", "cancel-replay")