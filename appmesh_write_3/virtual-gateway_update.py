#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-gateway.html
if __name__ == '__main__':
    """
	create-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-gateway.html
	delete-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-gateway.html
	describe-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-gateway.html
	list-virtual-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-gateways.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the virtual gateway resides in.
    # spec : 
    # virtual-gateway-name : The name of the virtual gateway to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "update-virtual-gateway", "mesh-name", "spec", "virtual-gateway-name", add_option_dict)
