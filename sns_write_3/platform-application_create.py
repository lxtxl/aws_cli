#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-platform-application.html
if __name__ == '__main__':
    """
	delete-platform-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-platform-application.html
	list-platform-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-platform-applications.html
    """

    parameter_display_string = """
    # name : Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.
    # platform : The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Firebase Cloud Messaging).
    # attributes : For a list of attributes, see SetPlatformApplicationAttributes
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sns", "create-platform-application", "name", "platform", "attributes", add_option_dict)
