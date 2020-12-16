#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/grant-permissions.html
if __name__ == '__main__':
    """
	list-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-permissions.html
	revoke-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/revoke-permissions.html
    """

    parameter_display_string = """
    # principal : 
    # resource : 
    # permissions : The permissions granted to the principal on the resource. AWS Lake Formation defines privileges to grant and revoke access to metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. AWS Lake Formation requires that each principal be authorized to perform a specific task on AWS Lake Formation resources.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lakeformation", "grant-permissions", "principal", "resource", "permissions", add_option_dict)
