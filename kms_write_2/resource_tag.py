#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/untag-resource.html
    """

    parameter_display_string = """
    # key-id : A unique identifier for the CMK you are tagging.
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # tags : One or more tags. Each tag consists of a tag key and a tag value.
(structure)

A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
For information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .
TagKey -> (string)

The key of the tag.

TagValue -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kms", "tag-resource", "key-id", "tags", add_option_dict)
