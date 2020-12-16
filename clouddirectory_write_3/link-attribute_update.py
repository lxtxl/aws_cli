#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-link-attributes.html
if __name__ == '__main__':
    """
	get-link-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-link-attributes.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see  arns or Typed Links .
    # typed-link-specifier : 
    # attribute-updates : The attributes update structure.
(structure)

Structure that contains attribute update information.
AttributeKey -> (structure)

The key of the attribute being updated.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


AttributeAction -> (structure)

The action to perform as part of the attribute update.
AttributeActionType -> (string)

A type that can be either UPDATE_OR_CREATE or DELETE .

AttributeUpdateValue -> (structure)

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
    write_three_parameter("clouddirectory", "update-link-attributes", "directory-arn", "typed-link-specifier", "attribute-updates", add_option_dict)
