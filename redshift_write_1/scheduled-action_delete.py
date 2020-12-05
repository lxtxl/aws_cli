#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-scheduled-action.html
if __name__ == '__main__':
    """
	create-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-scheduled-action.html
	describe-scheduled-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html
	modify-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-scheduled-action.html
    """

    parameter_display_string = """
    # scheduled-action-name : The name of the scheduled action to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "delete-scheduled-action", "scheduled-action-name", add_option_dict)





