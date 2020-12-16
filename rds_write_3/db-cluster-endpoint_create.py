#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-endpoint.html
if __name__ == '__main__':
    """
	delete-db-cluster-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-endpoint.html
	describe-db-cluster-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-endpoints.html
	modify-db-cluster-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-endpoint.html
    """

    parameter_display_string = """
    # db-cluster-identifier : The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.
    # db-cluster-endpoint-identifier : The identifier to use for the new endpoint. This parameter is stored as a lowercase string.
    # endpoint-type : The type of the endpoint. One of: READER , WRITER , ANY .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "create-db-cluster-endpoint", "db-cluster-identifier", "db-cluster-endpoint-identifier", "endpoint-type", add_option_dict)
