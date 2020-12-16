#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html
    """

    write_parameter("managedblockchain", "update-member")