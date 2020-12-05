#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/disassociate-qualification-from-worker.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # worker-id : The ID of the Worker who possesses the Qualification to be revoked.
    # qualification-type-id : The ID of the Qualification type of the Qualification to be revoked.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mturk", "disassociate-qualification-from-worker", "worker-id", "qualification-type-id", add_option_dict)
