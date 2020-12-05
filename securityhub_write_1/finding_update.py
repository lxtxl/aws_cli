#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-findings.html
if __name__ == '__main__':
    """
	get-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-findings.html
    """

    parameter_display_string = """
    # filters : Lists the secret request filters.
(structure)

Allows you to filter your list of secrets.
Key -> (string)

Filters your list of secrets by a specific key.

Values -> (list)

Filters your list of secrets by a specific value.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "update-findings", "filters", add_option_dict)





