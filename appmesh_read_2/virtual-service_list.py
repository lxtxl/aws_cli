#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-service.html
if __name__ == '__main__':
    """
	create-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-service.html
	delete-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-service.html
	list-virtual-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-services.html
	update-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-service.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the virtual service resides in.
    # virtual-service-name : The name of the virtual service to describe.
    """

    execute_two_parameter("appmesh", "describe-virtual-service", "mesh-name", "virtual-service-name", parameter_display_string)