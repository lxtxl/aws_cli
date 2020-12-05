#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/activate-event-source.html
if __name__ == '__main__':
    """
	deactivate-event-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/deactivate-event-source.html
	describe-event-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-event-source.html
	list-event-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-event-sources.html
    """

    parameter_display_string = """
    # name : The name of the partner event source to activate.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "activate-event-source", "name", add_option_dict)





