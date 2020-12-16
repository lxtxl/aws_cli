#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-node.html
	delete-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-node.html
	get-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html
	list-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-nodes.html
    """

    write_parameter("managedblockchain", "update-node")