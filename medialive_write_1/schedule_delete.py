#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-schedule.html
if __name__ == '__main__':
    """
	describe-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-schedule.html
    """

    parameter_display_string = """
    # channel-id : Id of the channel whose schedule is being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "delete-schedule", "channel-id", add_option_dict)





