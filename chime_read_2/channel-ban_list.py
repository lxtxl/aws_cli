#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-ban.html
if __name__ == '__main__':
    """
	create-channel-ban : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-ban.html
	delete-channel-ban : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-ban.html
	list-channel-bans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-bans.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel from which the user is banned.
    # member-arn : The ARN of the member being banned.
    """

    execute_two_parameter("chime", "describe-channel-ban", "channel-arn", "member-arn", parameter_display_string)