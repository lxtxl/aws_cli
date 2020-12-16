#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channels.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "delete-channel", "channel-arn", add_option_dict)





