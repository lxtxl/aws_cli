#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # entries : The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.
(structure)

Represents an event to be submitted.
Time -> (timestamp)

The time stamp of the event, per RFC3339 . If no time stamp is provided, the time stamp of the  PutEvents call is used.

Source -> (string)

The source of the event.

Resources -> (list)

AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
(string)

DetailType -> (string)

Free-form string used to decide what fields to expect in the event detail.

Detail -> (string)

A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.

EventBusName -> (string)

The event bus that will receive the event. Only the rules that are associated with this event bus will be able to match the event.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "put-events", "entries", add_option_dict)





