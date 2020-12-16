#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cluster-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-subnet-group.html
	describe-cluster-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-subnet-groups.html
	modify-cluster-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-subnet-group.html
    """

    write_parameter("redshift", "delete-cluster-subnet-group")