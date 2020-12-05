#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-or-update-tags.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # tags : One or more tags.
(structure)

Describes a tag for an Auto Scaling group.
ResourceId -> (string)

The name of the group.

ResourceType -> (string)

The type of resource. The only supported value is auto-scaling-group .

Key -> (string)

The tag key.

Value -> (string)

The tag value.

PropagateAtLaunch -> (boolean)

Determines whether the tag is added to new instances as they are launched in the group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("autoscaling", "create-or-update-tags", "tags", add_option_dict)





