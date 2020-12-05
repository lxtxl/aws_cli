#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-nodegroup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-nodegroup.html
	describe-nodegroup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-nodegroup.html
	list-nodegroups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-nodegroups.html
    """

    write_parameter("eks", "delete-nodegroup")