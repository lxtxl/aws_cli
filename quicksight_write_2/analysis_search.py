#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/search-analyses.html
if __name__ == '__main__':
    """
	list-analyses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-analyses.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the analyses that youâre searching for.
    # filters : The structure for the search filters that you want to apply to your search.
(structure)

A filter that you apply when searching for one or more analyses.
Operator -> (string)

The comparison operator that you want to use as a filter, for example "Operator": "StringEquals" .

Name -> (string)

The name of the value that you want to use as a filter, for example "Name": "QUICKSIGHT_USER" .

Value -> (string)

The value of the named item, in this case QUICKSIGHT_USER , that you want to use as a filter, for example "Value" . An example is "arn:aws:quicksight:us-east-1:1:user/default/UserName1" .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "search-analyses", "aws-account-id", "filters", add_option_dict)
