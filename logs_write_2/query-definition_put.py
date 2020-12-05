#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-query-definition.html
if __name__ == '__main__':
    """
	delete-query-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-query-definition.html
	describe-query-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-query-definitions.html
    """

    parameter_display_string = """
    # name : A name for the query definition. If you are saving a lot of query definitions, we recommend that you name them so that you can easily find the ones you want by using the first part of the name as a filter in the queryDefinitionNamePrefix parameter of DescribeQueryDefinitions .
    # query-string : The query string to use for this definition. For more information, see CloudWatch Logs Insights Query Syntax .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("logs", "put-query-definition", "name", "query-string", add_option_dict)
