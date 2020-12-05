#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-data-catalog.html
if __name__ == '__main__':
    """
	create-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html
	delete-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-data-catalog.html
	get-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-data-catalog.html
	list-data-catalogs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-data-catalogs.html
    """

    parameter_display_string = """
    # name : The name of the data catalog to update. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.
    # type : Specifies the type of data catalog to update. Specify LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore.
Possible values:

LAMBDA
GLUE
HIVE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("athena", "update-data-catalog", "name", "type", add_option_dict)
