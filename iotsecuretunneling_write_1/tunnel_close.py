#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/close-tunnel.html
if __name__ == '__main__':
    """
	describe-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/describe-tunnel.html
	list-tunnels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/list-tunnels.html
	open-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/open-tunnel.html
    """

    parameter_display_string = """
    # tunnel-id : The ID of the tunnel to close.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsecuretunneling", "close-tunnel", "tunnel-id", add_option_dict)





