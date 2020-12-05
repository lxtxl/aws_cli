#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/disassociate-node.html
if __name__ == '__main__':
    """
	associate-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/associate-node.html
    """

    parameter_display_string = """
    # server-name : The name of the server from which to disassociate the node.
    # node-name : The name of the client node.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks-cm", "disassociate-node", "server-name", "node-name", add_option_dict)
