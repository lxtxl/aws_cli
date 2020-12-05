#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-attendee.html
if __name__ == '__main__':
    """
	create-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-attendee.html
	delete-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-attendee.html
	list-attendees : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-attendees.html
	tag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-attendee.html
	untag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-attendee.html
    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    # attendee-id : The Amazon Chime SDK attendee ID.
    """

    execute_two_parameter("chime", "get-attendee", "meeting-id", "attendee-id", parameter_display_string)