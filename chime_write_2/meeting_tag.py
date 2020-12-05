#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-meeting.html
if __name__ == '__main__':
    """
	create-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-meeting.html
	delete-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-meeting.html
	get-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-meeting.html
	list-meetings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-meetings.html
	untag-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-meeting.html
    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    # tags : The tag key-value pairs.
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
    write_two_parameter("chime", "tag-meeting", "meeting-id", "tags", add_option_dict)
