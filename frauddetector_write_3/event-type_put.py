#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-event-type.html
if __name__ == '__main__':
    """
	delete-event-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-event-type.html
	get-event-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-types.html
    """

    parameter_display_string = """
    # name : The name.
    # event-variables : The event type variables.
(string)
    # entity-types : The entity type for the event type. Example entity types: customer, merchant, account.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("frauddetector", "put-event-type", "name", "event-variables", "entity-types", add_option_dict)
