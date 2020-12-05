#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-delivery-channel.html
if __name__ == '__main__':
    """
	describe-delivery-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html
	put-delivery-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-delivery-channel.html
    """

    parameter_display_string = """
    # delivery-channel-name : The name of the delivery channel to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "delete-delivery-channel", "delivery-channel-name", add_option_dict)





