#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource that you want to add one or more tags to.
    # tags : A list of the tags that you want to add to the resource. A tag consists of a required tag key (Key ) and an associated tag value (Value ). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.
(structure)

An object that defines the tags that are associated with a resource. A tag is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
Each tag consists of a required tag key and an associated tag value , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

Tag keys and values are case sensitive.
For each associated resource, each tag key must be unique and it can have only one value.
The aws: prefix is reserved for use by AWS; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix. Tags that use this prefix donât count against the limit of 50 tags per resource.
You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want a resource to have a specific tag value, donât specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint-email", "tag-resource", "resource-arn", "tags", add_option_dict)
