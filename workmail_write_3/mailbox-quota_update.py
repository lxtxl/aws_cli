#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-mailbox-quota.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier for the organization that contains the user for whom to update the mailbox quota.
    # user-id : The identifer for the user for whom to update the mailbox quota.
    # mailbox-quota : The updated mailbox quota, in MB, for the specified user.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "update-mailbox-quota", "organization-id", "user-id", "mailbox-quota", add_option_dict)
