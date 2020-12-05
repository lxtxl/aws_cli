#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-finding.html
if __name__ == '__main__':
    """
	list-audit-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-findings.html
    """

    parameter_display_string = """
    # finding-id : A unique identifier for a single audit finding. You can use this identifier to apply mitigation actions to the finding.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("iot", "describe-audit-finding", "finding-id", add_option_dict)