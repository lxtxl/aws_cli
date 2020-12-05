#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-gateway-group.html
if __name__ == '__main__':
    """
	create-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-gateway-group.html
	delete-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-gateway-group.html
	get-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-gateway-group.html
	list-gateway-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-gateway-groups.html
    """

    parameter_display_string = """
    # gateway-group-arn : The ARN of the gateway group to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "update-gateway-group", "gateway-group-arn", add_option_dict)





