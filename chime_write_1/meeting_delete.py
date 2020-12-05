#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-meeting.html
if __name__ == '__main__':
    """
	create-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-meeting.html
	get-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-meeting.html
	list-meetings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-meetings.html
	tag-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-meeting.html
	untag-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-meeting.html
    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "delete-meeting", "meeting-id", add_option_dict)





