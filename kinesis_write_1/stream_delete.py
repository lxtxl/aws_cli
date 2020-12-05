#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/delete-stream.html
if __name__ == '__main__':
    """
	create-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/create-stream.html
	describe-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-streams.html
    """

    parameter_display_string = """
    # stream-name : The name of the stream to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kinesis", "delete-stream", "stream-name", add_option_dict)





