#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/deregister-from-work-mail.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the Amazon WorkMail entity exists.
    # entity-id : The identifier for the member (user or group) to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "deregister-from-work-mail", "organization-id", "entity-id", add_option_dict)
