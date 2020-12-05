#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-tags-for-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-id : The ID of the resource with the tags to list.
You can specify any of the following taggable resources.

AWS account â specify the account ID number.
Organizational unit â specify the OU ID that begins with ou- and looks similar to: ``ou-1a2b-34uvwxyz ``
Root â specify the root ID that begins with r- and looks similar to: ``r-1a2b ``
Policy â specify the policy ID that begins with p- andlooks similar to: ``p-12abcdefg3 ``
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("organizations", "list-tags-for-resource", "resource-id", add_option_dict)