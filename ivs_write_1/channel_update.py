#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/update-channel.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-channel.html
	get-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-channels.html
    """

    parameter_display_string = """
    # arn : ARN of the channel to be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ivs", "update-channel", "arn", add_option_dict)





