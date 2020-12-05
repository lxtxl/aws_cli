#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/create-signaling-channel.html
if __name__ == '__main__':
    """
	delete-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/delete-signaling-channel.html
	describe-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/describe-signaling-channel.html
	list-signaling-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-signaling-channels.html
	update-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/update-signaling-channel.html
    """

    parameter_display_string = """
    # channel-name : A name for the signaling channel that you are creating. It must be unique for each AWS account and AWS Region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kinesisvideo", "create-signaling-channel", "channel-name", add_option_dict)




