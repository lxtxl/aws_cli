#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-conference-provider.html
if __name__ == '__main__':
    """
	create-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-conference-provider.html
	get-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-conference-provider.html
	list-conference-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-conference-providers.html
	update-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-conference-provider.html
    """

    parameter_display_string = """
    # conference-provider-arn : The ARN of the conference provider.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "delete-conference-provider", "conference-provider-arn", add_option_dict)





