#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html
if __name__ == '__main__':
    """
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-endpoint.html
	describe-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoints.html
	modify-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-endpoint.html
    """

    parameter_display_string = """
    # endpoint-identifier : The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They canât end with a hyphen, or contain two consecutive hyphens.
    # endpoint-type : The type of endpoint. Valid values are source and target .
Possible values:

source
target
    # engine-name : The type of engine for the endpoint. Valid values, depending on the EndpointType value, include "mysql" , "oracle" , "postgres" , "mariadb" , "aurora" , "aurora-postgresql" , "redshift" , "s3" , "db2" , "azuredb" , "sybase" , "dynamodb" , "mongodb" , "kinesis" , "kafka" , "elasticsearch" , "docdb" , "sqlserver" , and "neptune" .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("dms", "create-endpoint", "endpoint-identifier", "endpoint-type", "engine-name", add_option_dict)
