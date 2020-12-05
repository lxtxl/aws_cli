#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-gateway-group.html
if __name__ == '__main__':
    """
	delete-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-gateway-group.html
	get-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-gateway-group.html
	list-gateway-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-gateway-groups.html
	update-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-gateway-group.html
    """

    parameter_display_string = """
    # name : The name of the gateway group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "create-gateway-group", "name", add_option_dict)





