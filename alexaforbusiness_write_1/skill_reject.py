#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/reject-skill.html
if __name__ == '__main__':
    """
	approve-skill : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/approve-skill.html
	list-skills : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-skills.html
    """

    parameter_display_string = """
    # skill-id : The unique identifier of the skill.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "reject-skill", "skill-id", add_option_dict)





