#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-membership-for-app-instance-user.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel to which the user belongs.
    # app-instance-user-arn : The ARN of the user in a channel.
    """

    execute_two_parameter("chime", "describe-channel-membership-for-app-instance-user", "channel-arn", "app-instance-user-arn", parameter_display_string)