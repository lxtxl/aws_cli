#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-insight.html
if __name__ == '__main__':
    """
	create-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-insight.html
	get-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insights.html
	update-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-insight.html
    """

    parameter_display_string = """
    # insight-arn : The ARN of the insight to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "delete-insight", "insight-arn", add_option_dict)





