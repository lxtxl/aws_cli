#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/delete-target.html
if __name__ == '__main__':
    """
	list-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-targets.html
    """

    parameter_display_string = """
    # target-address : The Amazon Resource Name (ARN) of the SNS topic to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codestar-notifications", "delete-target", "target-address", add_option_dict)





