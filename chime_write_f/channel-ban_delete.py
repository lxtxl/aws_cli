#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-channel-ban : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-ban.html
	describe-channel-ban : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-ban.html
	list-channel-bans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-bans.html
    """

    write_parameter("chime", "delete-channel-ban")