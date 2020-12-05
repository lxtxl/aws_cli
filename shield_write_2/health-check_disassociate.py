#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/disassociate-health-check.html
if __name__ == '__main__':
    """
	associate-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/associate-health-check.html
    """

    parameter_display_string = """
    # protection-id : The unique identifier (ID) for the  Protection object to remove the health check association from.
    # health-check-arn : The Amazon Resource Name (ARN) of the health check that is associated with the protection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("shield", "disassociate-health-check", "protection-id", "health-check-arn", add_option_dict)
