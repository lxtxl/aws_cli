#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-service.html
	delete-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-service.html
	describe-virtual-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-service.html
	list-virtual-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-services.html
    """

    write_parameter("appmesh", "update-virtual-service")