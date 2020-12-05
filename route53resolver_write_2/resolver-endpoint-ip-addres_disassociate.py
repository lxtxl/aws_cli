#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-endpoint-ip-address.html
if __name__ == '__main__':
    """
	associate-resolver-endpoint-ip-address : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-endpoint-ip-address.html
    """

    parameter_display_string = """
    # resolver-endpoint-id : The ID of the Resolver endpoint that you want to disassociate an IP address from.
    # ip-address : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53resolver", "disassociate-resolver-endpoint-ip-address", "resolver-endpoint-id", "ip-address", add_option_dict)
