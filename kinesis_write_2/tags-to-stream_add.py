#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/add-tags-to-stream.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stream-name : The name of the stream.
    # tags : A set of up to 10 key-value pairs to use to create the tags.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "add-tags-to-stream", "stream-name", "tags", add_option_dict)
