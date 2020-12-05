#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-create-attendee.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    # attendees : The request containing the attendees to create.
(structure)

The Amazon Chime SDK attendee fields to create, used with the BatchCreateAttendee action.
ExternalUserId -> (string)

The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.

Tags -> (list)

The tag key-value pairs.
(structure)

Describes a tag applied to a resource.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "batch-create-attendee", "meeting-id", "attendees", add_option_dict)
