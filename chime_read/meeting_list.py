#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-meetings.html
if __name__ == '__main__':
    """
	create-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-meeting.html
	delete-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-meeting.html
	get-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-meeting.html
	tag-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-meeting.html
	untag-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-meeting.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("chime", "list-meetings", add_option_dict)