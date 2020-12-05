#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-insight-selectors.html
if __name__ == '__main__':
    """
	get-insight-selectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-insight-selectors.html
    """

    parameter_display_string = """
    # trail-name : The name of the CloudTrail trail for which you want to change or add Insights selectors.
    # insight-selectors : A JSON string that contains the insight types you want to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.
(structure)

A JSON string that contains a list of insight types that are logged on a trail.
InsightType -> (string)

The type of insights to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudtrail", "put-insight-selectors", "trail-name", "insight-selectors", add_option_dict)
