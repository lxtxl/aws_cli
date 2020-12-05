#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/remove-tags-from-certificate.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # certificate-arn : String that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:

arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012

For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    # tags : The key-value pair that defines the tag to remove.
(structure)

A key-value pair that identifies or specifies metadata about an ACM resource.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm", "remove-tags-from-certificate", "certificate-arn", "tags", add_option_dict)
