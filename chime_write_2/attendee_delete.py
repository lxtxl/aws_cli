#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-attendee.html
if __name__ == '__main__':
    """
	create-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-attendee.html
	get-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-attendee.html
	list-attendees : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-attendees.html
	tag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-attendee.html
	untag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-attendee.html
    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    # attendee-id : The Amazon Chime SDK attendee ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "delete-attendee", "meeting-id", "attendee-id", add_option_dict)
