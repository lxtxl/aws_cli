#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/get-discovered-schema.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # events : An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events.
(string)
    # type : The type of event.
Possible values:

OpenApi3
JSONSchemaDraft4
    """

    execute_two_parameter("schemas", "get-discovered-schema", "events", "type", parameter_display_string)