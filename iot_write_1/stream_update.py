#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-stream.html
if __name__ == '__main__':
    """
	create-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-stream.html
	delete-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-stream.html
	describe-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-streams.html
    """

    parameter_display_string = """
    # stream-id : The stream ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "update-stream", "stream-id", add_option_dict)





