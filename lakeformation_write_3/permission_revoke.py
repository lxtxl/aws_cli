#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/revoke-permissions.html
if __name__ == '__main__':
    """
	grant-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/grant-permissions.html
	list-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-permissions.html
    """

    parameter_display_string = """
    # principal : 
    # resource : 
    # permissions : The permissions revoked to the principal on the resource. For information about permissions, see Security and Access Control to Metadata and Data .
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lakeformation", "revoke-permissions", "principal", "resource", "permissions", add_option_dict)
