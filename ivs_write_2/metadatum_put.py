#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/put-metadata.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # channel-arn : ARN of the channel into which metadata is inserted. This channel must have an active stream.
    # metadata : Metadata to insert into the stream. Maximum: 1 KB per request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ivs", "put-metadata", "channel-arn", "metadata", add_option_dict)
