#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-mesh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-mesh.html
	delete-mesh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-mesh.html
	describe-mesh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-mesh.html
	list-meshes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-meshes.html
    """

    write_parameter("appmesh", "update-mesh")