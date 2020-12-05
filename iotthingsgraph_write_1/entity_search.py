#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-entities.html
if __name__ == '__main__':
    """
	get-entities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-entities.html
    """

    parameter_display_string = """
    # entity-types : The entity types for which to search.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotthingsgraph", "search-entities", "entity-types", add_option_dict)





