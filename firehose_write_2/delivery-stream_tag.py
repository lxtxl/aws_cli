#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/tag-delivery-stream.html
if __name__ == '__main__':
    """
	create-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/create-delivery-stream.html
	delete-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/delete-delivery-stream.html
	describe-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html
	list-delivery-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/list-delivery-streams.html
	untag-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/untag-delivery-stream.html
    """

    parameter_display_string = """
    # delivery-stream-name : The name of the delivery stream to which you want to add the tags.
    # tags : A set of key-value pairs to use to create the tags.
(structure)

Metadata that you can assign to a delivery stream, consisting of a key-value pair.
Key -> (string)

A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

Value -> (string)

An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("firehose", "tag-delivery-stream", "delivery-stream-name", "tags", add_option_dict)
