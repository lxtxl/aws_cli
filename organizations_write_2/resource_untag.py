#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/tag-resource.html
    """

    parameter_display_string = """
    # resource-id : The ID of the resource to remove a tag from.
You can specify any of the following taggable resources.

AWS account â specify the account ID number.
Organizational unit â specify the OU ID that begins with ou- and looks similar to: ``ou-1a2b-34uvwxyz ``
Root â specify the root ID that begins with r- and looks similar to: ``r-1a2b ``
Policy â specify the policy ID that begins with p- andlooks similar to: ``p-12abcdefg3 ``
    # tag-keys : The list of keys for tags to remove from the specified resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "untag-resource", "resource-id", "tag-keys", add_option_dict)
