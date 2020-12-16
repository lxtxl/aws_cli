#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-named-query.html
if __name__ == '__main__':
    """
	delete-named-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-named-query.html
	get-named-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-named-query.html
	list-named-queries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-named-queries.html
    """

    parameter_display_string = """
    # name : The query name.
    # database : The database to which the query belongs.
    # query-string : The contents of the query with all query statements.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("athena", "create-named-query", "name", "database", "query-string", add_option_dict)
