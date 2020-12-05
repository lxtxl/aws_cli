#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/associate-repository.html
if __name__ == '__main__':
    """
	disassociate-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/disassociate-repository.html
    """

    parameter_display_string = """
    # repository : The name of the repository to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codeguru-reviewer", "associate-repository", "repository", add_option_dict)





