#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/close-instance-public-ports.html
if __name__ == '__main__':
    """
	open-instance-public-ports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/open-instance-public-ports.html
	put-instance-public-ports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-instance-public-ports.html
    """

    parameter_display_string = """
    # port-info : 
    # instance-name : The name of the instance for which to close ports.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "close-instance-public-ports", "port-info", "instance-name", add_option_dict)
