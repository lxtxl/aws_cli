#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/notify-workers.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # subject : The subject line of the email message to send. Can include up to 200 characters.
    # message-text : The text of the email message to send. Can include up to 4,096 characters
    # worker-ids : A list of Worker IDs you wish to notify. You can notify upto 100 Workers at a time.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("mturk", "notify-workers", "subject", "message-text", "worker-ids", add_option_dict)
