#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-platform-application.html
if __name__ == '__main__':
    """
	create-platform-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-platform-application.html
	list-platform-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-platform-applications.html
    """

    parameter_display_string = """
    # platform-application-arn : PlatformApplicationArn of platform application object to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sns", "delete-platform-application", "platform-application-arn", add_option_dict)





