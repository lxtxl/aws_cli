#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/accept-reserved-node-exchange.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # reserved-node-id : A string representing the node identifier of the DC1 Reserved Node to be exchanged.
    # target-reserved-node-offering-id : The unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling  GetReservedNodeExchangeOfferings
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "accept-reserved-node-exchange", "reserved-node-id", "target-reserved-node-offering-id", add_option_dict)
