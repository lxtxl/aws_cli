#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-worker-block.html
if __name__ == '__main__':
    """
	create-worker-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-worker-block.html
	list-worker-blocks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-worker-blocks.html
    """

    parameter_display_string = """
    # worker-id : The ID of the Worker to unblock.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mturk", "delete-worker-block", "worker-id", add_option_dict)





