#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-attendee-tags.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    # attendee-id : The Amazon Chime SDK attendee ID.
    """

    execute_two_parameter("chime", "list-attendee-tags", "meeting-id", "attendee-id", parameter_display_string)