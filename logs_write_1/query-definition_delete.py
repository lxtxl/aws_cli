#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-query-definition.html
if __name__ == '__main__':
    """
	describe-query-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-query-definitions.html
	put-query-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-query-definition.html
    """

    parameter_display_string = """
    # query-definition-id : The ID of the query definition that you want to delete. You can use DescribeQueryDefinitions to retrieve the IDs of your saved query definitions.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("logs", "delete-query-definition", "query-definition-id", add_option_dict)





