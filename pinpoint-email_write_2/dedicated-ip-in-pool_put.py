#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-dedicated-ip-in-pool.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # ip : The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address thatâs associated with your Amazon Pinpoint account.
    # destination-pool-name : The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint-email", "put-dedicated-ip-in-pool", "ip", "destination-pool-name", add_option_dict)
