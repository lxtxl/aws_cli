#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/associate-qualification-with-worker.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # qualification-type-id : The ID of the Qualification type to use for the assigned Qualification.
    # worker-id : The ID of the Worker to whom the Qualification is being assigned. Worker IDs are included with submitted HIT assignments and Qualification requests.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mturk", "associate-qualification-with-worker", "qualification-type-id", "worker-id", add_option_dict)
