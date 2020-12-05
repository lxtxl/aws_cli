#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/untag-resource.html
    """

    parameter_display_string = """
    # resource-id : The ID of the resource to add a tag to.
    # tags : A list of tags to add to the specified resource.
You can specify any of the following taggable resources.

AWS account â specify the account ID number.
Organizational unit â specify the OU ID that begins with ou- and looks similar to: ``ou-1a2b-34uvwxyz ``
Root â specify the root ID that begins with r- and looks similar to: ``r-1a2b ``
Policy â specify the policy ID that begins with p- andlooks similar to: ``p-12abcdefg3 ``

For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you canât set it to null .

Note
If any one of the tags is invalid or if you exceed the allowed number of tags for an account user, then the entire request fails and the account is not created.

(structure)

A custom key-value pair associated with a resource within your organization.
You can attach tags to any of the following organization resources.

AWS account
Organizational unit (OU)
Organization root
Policy

Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value thatâs associated with the key of the tag. You can set the value of a tag to an empty string, but you canât set the value of a tag to null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "tag-resource", "resource-id", "tags", add_option_dict)
