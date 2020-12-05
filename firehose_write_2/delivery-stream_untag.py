#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/untag-delivery-stream.html
if __name__ == '__main__':
    """
	create-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/create-delivery-stream.html
	delete-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/delete-delivery-stream.html
	describe-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html
	list-delivery-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/list-delivery-streams.html
	tag-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/tag-delivery-stream.html
    """

    parameter_display_string = """
    # delivery-stream-name : The name of the delivery stream.
    # tag-keys : A list of tag keys. Each corresponding tag is removed from the delivery stream.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("firehose", "untag-delivery-stream", "delivery-stream-name", "tag-keys", add_option_dict)
