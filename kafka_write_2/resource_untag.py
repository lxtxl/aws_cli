#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) that uniquely identifies the resource thatâs associated with the tags.
    # tag-keys : Tag keys must be unique for a given cluster. In addition, the following restrictions apply:

Each tag key must be unique. If you add a tag with a key thatâs already in use, your new tag overwrites the existing key-value pair.
You canât start a tag key with aws: because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you canât edit or delete them.
Tag keys must be between 1 and 128 Unicode characters in length.
Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: _ . / = + - @.


(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kafka", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
