#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-route.html
	describe-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html
	list-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-routes.html
	update-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-route.html
    """

    write_parameter("appmesh", "delete-route")