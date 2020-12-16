#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-listener.html
if __name__ == '__main__':
    """
	delete-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-listener.html
	describe-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-listener.html
	list-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-listeners.html
	update-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-listener.html
    """

    parameter_display_string = """
    # accelerator-arn : The Amazon Resource Name (ARN) of your accelerator.
    # port-ranges : The list of port ranges to support for connections from clients to your accelerator.
(structure)

A complex type for a range of ports for a listener.
FromPort -> (integer)

The first port in the range of ports, inclusive.

ToPort -> (integer)

The last port in the range of ports, inclusive.
    # protocol : The protocol for connections from clients to your accelerator.
Possible values:

TCP
UDP
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("globalaccelerator", "create-listener", "accelerator-arn", "port-ranges", "protocol", add_option_dict)
