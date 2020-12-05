#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/delete-outpost.html
if __name__ == '__main__':
    """
	create-outpost : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/create-outpost.html
	get-outpost : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/get-outpost.html
	list-outposts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/list-outposts.html
    """

    parameter_display_string = """
    # outpost-id : The ID of the Outpost.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("outposts", "delete-outpost", "outpost-id", add_option_dict)





