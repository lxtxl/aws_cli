#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-member-session.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # id : The unique identifier for the Amazon Macie resource or account that the request applies to.
    # status : Specifies the new status for the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.
Possible values:

PAUSED
ENABLED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("macie2", "update-member-session", "id", "status", add_option_dict)
