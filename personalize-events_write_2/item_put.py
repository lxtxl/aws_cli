#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-events/put-items.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # dataset-arn : The Amazon Resource Number (ARN) of the Items dataset you are adding the item or items to.
    # items : A list of item data.
(structure)

Represents item metadata added to an Items dataset using the PutItems API.
itemId -> (string)

The ID associated with the item.

properties -> (string)

A string map of item-specific metadata. Each element in the map consists of a key-value pair. For example,

{"numberOfRatings": "12"}

The keys use camel case names that match the fields in the Items schema. In the above example, the numberOfRatings would match the âNUMBER_OF_RATINGSâ field defined in the Items schema.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("personalize-events", "put-items", "dataset-arn", "items", add_option_dict)
