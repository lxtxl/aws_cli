#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-membership.html
if __name__ == '__main__':
    """
	create-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-membership.html
	delete-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-membership.html
	list-channel-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-memberships.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel.
    # member-arn : The ARN of the member.
    """

    execute_two_parameter("chime", "describe-channel-membership", "channel-arn", "member-arn", parameter_display_string)