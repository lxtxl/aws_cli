#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-node.html
	describe-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-node.html
	list-virtual-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-nodes.html
	update-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-node.html
    """

    write_parameter("appmesh", "delete-virtual-node")