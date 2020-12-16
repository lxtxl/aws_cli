#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html
	describe-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html
	list-virtual-routers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html
	update-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html
    """

    write_parameter("appmesh", "delete-virtual-router")