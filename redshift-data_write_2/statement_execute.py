#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/execute-statement.html
if __name__ == '__main__':
    """
	cancel-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/cancel-statement.html
	describe-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/describe-statement.html
	list-statements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/list-statements.html
    """

    parameter_display_string = """
    # cluster-identifier : The cluster identifier. This parameter is required when authenticating using either AWS Secrets Manager or temporary credentials.
    # sql : The SQL statement text to run.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift-data", "execute-statement", "cluster-identifier", "sql", add_option_dict)
