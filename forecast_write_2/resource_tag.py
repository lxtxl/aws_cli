#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Forecast dataset groups, datasets, dataset import jobs, predictors, forecasts, and forecast export jobs.
    # tags : The tags to add to the resource. A tag is an array of key-value pairs.
The following basic restrictions apply to tags:

Maximum number of tags per resource - 50.
For each resource, each tag key must be unique, and each tag key can have only one value.
Maximum key length - 128 Unicode characters in UTF-8.
Maximum value length - 256 Unicode characters in UTF-8.
If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
Tag keys and values are case sensitive.
Do not use aws: , AWS: , or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.

(structure)

The optional metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
The following basic restrictions apply to tags:

Maximum number of tags per resource - 50.
For each resource, each tag key must be unique, and each tag key can have only one value.
Maximum key length - 128 Unicode characters in UTF-8.
Maximum value length - 256 Unicode characters in UTF-8.
If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
Tag keys and values are case sensitive.
Do not use aws: , AWS: , or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.

Key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

Value -> (string)

The optional part of a key-value pair that makes up a tag. A value acts as a descriptor within a tag category (key).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("forecast", "tag-resource", "resource-arn", "tags", add_option_dict)
