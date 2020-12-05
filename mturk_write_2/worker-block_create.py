#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-worker-block.html
if __name__ == '__main__':
    """
	delete-worker-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-worker-block.html
	list-worker-blocks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-worker-blocks.html
    """

    parameter_display_string = """
    # worker-id : The ID of the Worker to block.
    # reason : A message explaining the reason for blocking the Worker. This parameter enables you to keep track of your Workers. The Worker does not see this message.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mturk", "create-worker-block", "worker-id", "reason", add_option_dict)
