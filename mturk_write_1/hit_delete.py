#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-hit.html
if __name__ == '__main__':
    """
	create-hit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-hit.html
	get-hit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-hit.html
	list-hits : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-hits.html
    """

    parameter_display_string = """
    # hit-id : The ID of the HIT to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mturk", "delete-hit", "hit-id", add_option_dict)





