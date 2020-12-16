#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/put-repository-catalog-data.html
if __name__ == '__main__':
    """
	get-repository-catalog-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/get-repository-catalog-data.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository to create or update the catalog data for.
    # catalog-data : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecr-public", "put-repository-catalog-data", "repository-name", "catalog-data", add_option_dict)
