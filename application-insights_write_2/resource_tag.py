#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the application that you want to add one or more tags to.
    # tags : A list of tags that to add to the application. A tag consists of a required tag key (Key ) and an associated tag value (Value ). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.
(structure)

An object that defines the tags associated with an application. A tag is a label that you optionally define and associate with an application. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria.
Each tag consists of a required tag key and an associated tag value , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

Tag keys and values are case sensitive.
For each associated resource, each tag key must be unique and it can have only one value.
The aws: prefix is reserved for use by AWS; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want an application to have a specific tag value, donât specify a value for this parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("application-insights", "tag-resource", "resource-arn", "tags", add_option_dict)
