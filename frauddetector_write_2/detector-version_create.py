#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-detector-version.html
if __name__ == '__main__':
    """
	delete-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector-version.html
	get-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detector-version.html
	update-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version.html
    """

    parameter_display_string = """
    # detector-id : The ID of the detector under which you want to create a new version.
    # rules : The rules to include in the detector version.
(structure)

A rule.
detectorId -> (string)

The detector for which the rule is associated.

ruleId -> (string)

The rule ID.

ruleVersion -> (string)

The rule version.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("frauddetector", "create-detector-version", "detector-id", "rules", add_option_dict)
