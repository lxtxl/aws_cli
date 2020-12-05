#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/stop-channel.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-channels.html
	start-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-channel.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-channel.html
    """

    parameter_display_string = """
    # channel-id : A request to stop a running channel
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "stop-channel", "channel-id", add_option_dict)





