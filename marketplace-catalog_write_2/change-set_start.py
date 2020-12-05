#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html
if __name__ == '__main__':
    """
	cancel-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/cancel-change-set.html
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html
    """

    parameter_display_string = """
    # catalog : The catalog related to the request. Fixed value: AWSMarketplace
    # change-set : Array of change object.
(structure)

An object that contains the ChangeType , Details , and Entity .
ChangeType -> (string)

Change types are single string values that describe your intention for the change. Each change type is unique for each EntityType provided in the changeâs scope.

Entity -> (structure)

The entity to be changed.
Type -> (string)

The type of entity.

Identifier -> (string)

The identifier for the entity.


Details -> (string)

This object contains details specific to the change type of the requested change.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("marketplace-catalog", "start-change-set", "catalog", "change-set", add_option_dict)
