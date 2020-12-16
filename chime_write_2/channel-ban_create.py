#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-ban.html
if __name__ == '__main__':
    """
	delete-channel-ban : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-ban.html
	describe-channel-ban : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-ban.html
	list-channel-bans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-bans.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the ban request.
    # member-arn : The ARN of the member being banned.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "create-channel-ban", "channel-arn", "member-arn", add_option_dict)
