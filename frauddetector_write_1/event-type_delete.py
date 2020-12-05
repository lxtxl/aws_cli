#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-event-type.html
if __name__ == '__main__':
    """
	get-event-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-types.html
	put-event-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-event-type.html
    """

    parameter_display_string = """
    # name : The name of the event type to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("frauddetector", "delete-event-type", "name", add_option_dict)





