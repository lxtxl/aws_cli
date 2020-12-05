#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/remove-tags-from-stream.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stream-name : The name of the stream.
    # tag-keys : A list of tag keys. Each corresponding tag is removed from the stream.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "remove-tags-from-stream", "stream-name", "tag-keys", add_option_dict)
