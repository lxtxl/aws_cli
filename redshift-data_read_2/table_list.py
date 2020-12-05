#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/list-tables.html
if __name__ == '__main__':
    """
	describe-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/describe-table.html
    """

    parameter_display_string = """
    # cluster-identifier : The cluster identifier. This parameter is required when authenticating using either AWS Secrets Manager or temporary credentials.
    # database : The name of the database. This parameter is required when authenticating using temporary credentials.
    """

    execute_two_parameter("redshift-data", "list-tables", "cluster-identifier", "database", parameter_display_string)