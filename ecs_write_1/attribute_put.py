#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/put-attributes.html
if __name__ == '__main__':
    """
	delete-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-attributes.html
	list-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-attributes.html
    """

    parameter_display_string = """
    # attributes : The attributes to apply to your resource. You can specify up to 10 custom attributes per resource. You can specify up to 10 attributes in a single call.
(structure)

An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see Attributes in the Amazon Elastic Container Service Developer Guide .
name -> (string)

The name of the attribute. The name must contain between 1 and 128 characters and name may contain letters (uppercase and lowercase), numbers, hyphens, underscores, forward slashes, back slashes, or periods.

value -> (string)

The value of the attribute. The value must contain between 1 and 128 characters and may contain letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, back slashes, colons, or spaces. The value cannot contain any leading or trailing whitespace.

targetType -> (string)

The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

targetId -> (string)

The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "put-attributes", "attributes", add_option_dict)





