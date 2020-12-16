#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/add-notification-channel.html
if __name__ == '__main__':
    """
	list-notification-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-notification-channels.html
	remove-notification-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/remove-notification-channel.html
    """

    parameter_display_string = """
    # config : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devops-guru", "add-notification-channel", "config", add_option_dict)





