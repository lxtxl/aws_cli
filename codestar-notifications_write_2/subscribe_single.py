#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/subscribe.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the notification rule for which you want to create the association.
    # target : The target for the route.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codestar-notifications", "subscribe", "arn", "target", add_option_dict)
