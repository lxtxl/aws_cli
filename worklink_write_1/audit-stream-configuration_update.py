#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/update-audit-stream-configuration.html
if __name__ == '__main__':
    """
	describe-audit-stream-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-audit-stream-configuration.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("worklink", "update-audit-stream-configuration", "fleet-arn", add_option_dict)





