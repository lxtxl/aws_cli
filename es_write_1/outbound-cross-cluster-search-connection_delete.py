#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-outbound-cross-cluster-search-connection.html
if __name__ == '__main__':
    """
	create-outbound-cross-cluster-search-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-outbound-cross-cluster-search-connection.html
	describe-outbound-cross-cluster-search-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-outbound-cross-cluster-search-connections.html
    """

    parameter_display_string = """
    # cross-cluster-search-connection-id : The id of the outbound connection that you want to permanently delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("es", "delete-outbound-cross-cluster-search-connection", "cross-cluster-search-connection-id", add_option_dict)





