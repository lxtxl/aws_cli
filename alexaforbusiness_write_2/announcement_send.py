#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/send-announcement.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # room-filters : The filters to use to send an announcement to a specified list of rooms. The supported filter keys are RoomName, ProfileName, RoomArn, and ProfileArn. To send to all rooms, specify an empty RoomFilters list.
(structure)

A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
Key -> (string)

The key of a filter.

Values -> (list)

The values of a filter.
(string)
    # content : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "send-announcement", "room-filters", "content", add_option_dict)
