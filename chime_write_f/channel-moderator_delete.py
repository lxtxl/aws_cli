#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-channel-moderator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-moderator.html
	describe-channel-moderator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-moderator.html
	list-channel-moderators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-moderators.html
    """

    write_parameter("chime", "delete-channel-moderator")