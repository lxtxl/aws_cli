#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/revoke-domain-access.html
if __name__ == '__main__':
    """
	restore-domain-access : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/restore-domain-access.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # domain-name : The name of the domain.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("worklink", "revoke-domain-access", "fleet-arn", "domain-name", add_option_dict)
