#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-addon.html
	delete-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-addon.html
	describe-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-addon.html
	list-addons : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-addons.html
    """

    write_parameter("eks", "update-addon")