#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-endpoint.html
if __name__ == '__main__':
    """
	create-db-cluster-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-endpoint.html
	delete-db-cluster-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-endpoint.html
	describe-db-cluster-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-endpoints.html
    """

    parameter_display_string = """
    # db-cluster-endpoint-identifier : The identifier of the endpoint to modify. This parameter is stored as a lowercase string.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "modify-db-cluster-endpoint", "db-cluster-endpoint-identifier", add_option_dict)





