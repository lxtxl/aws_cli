#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-membership.html
if __name__ == '__main__':
    """
	delete-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-membership.html
	describe-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-membership.html
	list-channel-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-memberships.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel to which youâre adding users.
    # member-arn : The ARN of the member you want to add to the channel.
    # type : The membership type of a user, DEFAULT or HIDDEN . Default members are always returned as part of ListChannelMemberships . Hidden members are only returned if the type filter in ListChannelMemberships equals HIDDEN . Otherwise hidden members are not returned. This is only supported by moderators.
Possible values:

DEFAULT
HIDDEN
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "create-channel-membership", "channel-arn", "member-arn", "type", add_option_dict)
