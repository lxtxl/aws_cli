#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-hapg : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-hapg.html
	describe-hapg : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-hapg.html
	list-hapgs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-hapgs.html
	modify-hapg : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/modify-hapg.html
    """

    write_parameter("cloudhsm", "delete-hapg")