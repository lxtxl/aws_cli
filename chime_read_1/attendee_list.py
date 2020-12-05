#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-attendees.html
if __name__ == '__main__':
    """
	create-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-attendee.html
	delete-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-attendee.html
	get-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-attendee.html
	tag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-attendee.html
	untag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-attendee.html
    """

    parameter_display_string = """
    # meeting-id : The Amazon Chime SDK meeting ID.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("chime", "list-attendees", "meeting-id", add_option_dict)