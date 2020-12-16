#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-object-attributes.html
if __name__ == '__main__':
    """
	get-object-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-object-attributes.html
	list-object-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-object-attributes.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
    # object-reference : 
    # attribute-updates : The attributes update structure.
(structure)

Structure that contains attribute update information.
ObjectAttributeKey -> (structure)

The key of the attribute being updated.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


ObjectAttributeAction -> (structure)

The action to perform as part of the attribute update.
ObjectAttributeActionType -> (string)

A type that can be either Update or Delete .

ObjectAttributeUpdateValue -> (structure)

The value that you want to update to.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("clouddirectory", "update-object-attributes", "directory-arn", "object-reference", "attribute-updates", add_option_dict)
