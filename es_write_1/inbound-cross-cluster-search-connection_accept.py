#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/accept-inbound-cross-cluster-search-connection.html
if __name__ == '__main__':
    """
	delete-inbound-cross-cluster-search-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-inbound-cross-cluster-search-connection.html
	describe-inbound-cross-cluster-search-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-inbound-cross-cluster-search-connections.html
	reject-inbound-cross-cluster-search-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/reject-inbound-cross-cluster-search-connection.html
    """

    parameter_display_string = """
    # cross-cluster-search-connection-id : The id of the inbound connection that you want to accept.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("es", "accept-inbound-cross-cluster-search-connection", "cross-cluster-search-connection-id", add_option_dict)





