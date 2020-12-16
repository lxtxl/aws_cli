#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-membership.html
if __name__ == '__main__':
    """
	create-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-membership.html
	describe-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-membership.html
	list-channel-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-memberships.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel from which you want to remove the user.
    # member-arn : The ARN of the member that youâre removing from the channel.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "delete-channel-membership", "channel-arn", "member-arn", add_option_dict)
