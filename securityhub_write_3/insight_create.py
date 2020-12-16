#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-insight.html
if __name__ == '__main__':
    """
	delete-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-insight.html
	get-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insights.html
	update-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-insight.html
    """

    parameter_display_string = """
    # name : The name of the custom insight to create.
    # filters : Lists the secret request filters.
(structure)

Allows you to filter your list of secrets.
Key -> (string)

Filters your list of secrets by a specific key.

Values -> (list)

Filters your list of secrets by a specific value.
(string)
    # group-by-attribute : The attribute used to group the findings for the insight. The grouping attribute identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("securityhub", "create-insight", "name", "filters", "group-by-attribute", add_option_dict)
