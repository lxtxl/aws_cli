#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/get-data-endpoint.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # api-name : The name of the API action for which to get an endpoint.
Possible values:

PUT_MEDIA
GET_MEDIA
LIST_FRAGMENTS
GET_MEDIA_FOR_FRAGMENT_LIST
GET_HLS_STREAMING_SESSION_URL
GET_DASH_STREAMING_SESSION_URL
GET_CLIP
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

    execute_one_parameter("kinesisvideo", "get-data-endpoint", "api-name", add_option_dict)