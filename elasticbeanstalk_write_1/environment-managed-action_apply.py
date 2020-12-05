#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/apply-environment-managed-action.html
if __name__ == '__main__':
    """
	describe-environment-managed-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environment-managed-actions.html
    """

    parameter_display_string = """
    # action-id : The action ID of the scheduled managed action to execute.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticbeanstalk", "apply-environment-managed-action", "action-id", add_option_dict)





