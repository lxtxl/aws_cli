#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-stream-key.html
if __name__ == '__main__':
    """
	delete-stream-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-stream-key.html
	get-stream-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-key.html
	list-stream-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-stream-keys.html
    """

    parameter_display_string = """
    # channel-arn : ARN of the channel for which to create the stream key.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ivs", "create-stream-key", "channel-arn", add_option_dict)





