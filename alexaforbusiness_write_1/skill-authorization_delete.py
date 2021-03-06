#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-skill-authorization.html
if __name__ == '__main__':
    """
	put-skill-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/put-skill-authorization.html
    """

    parameter_display_string = """
    # skill-id : The unique identifier of a skill.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "delete-skill-authorization", "skill-id", add_option_dict)





