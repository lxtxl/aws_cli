#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-moderator.html
if __name__ == '__main__':
    """
	create-channel-moderator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-moderator.html
	describe-channel-moderator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-moderator.html
	list-channel-moderators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-moderators.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel.
    # channel-moderator-arn : The ARN of the moderator being deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "delete-channel-moderator", "channel-arn", "channel-moderator-arn", add_option_dict)
