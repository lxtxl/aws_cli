#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html
if __name__ == '__main__':
    """
	create-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html
	delete-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-router.html
	list-virtual-routers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html
	update-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the virtual router resides in.
    # virtual-router-name : The name of the virtual router to describe.
    """

    execute_two_parameter("appmesh", "describe-virtual-router", "mesh-name", "virtual-router-name", parameter_display_string)