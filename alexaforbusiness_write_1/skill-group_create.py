#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-skill-group.html
if __name__ == '__main__':
    """
	delete-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-skill-group.html
	get-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-skill-group.html
	search-skill-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-skill-groups.html
	update-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-skill-group.html
    """

    parameter_display_string = """
    # skill-group-name : The name for the skill group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "create-skill-group", "skill-group-name", add_option_dict)





