#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/stop-stream.html
if __name__ == '__main__':
    """
	get-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-streams.html
    """

    parameter_display_string = """
    # channel-arn : ARN of the channel for which the stream is to be stopped.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ivs", "stop-stream", "channel-arn", add_option_dict)





