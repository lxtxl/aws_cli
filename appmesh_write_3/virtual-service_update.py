#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-service.html
if __name__ == '__main__':
    """
	create-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-service.html
	delete-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-service.html
	describe-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-service.html
	list-virtual-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-services.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the virtual service resides in.
    # spec : 
    # virtual-service-name : The name of the virtual service to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "update-virtual-service", "mesh-name", "spec", "virtual-service-name", add_option_dict)
