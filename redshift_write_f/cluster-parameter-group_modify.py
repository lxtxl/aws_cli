#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-parameter-group.html
	delete-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-parameter-group.html
	describe-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameter-groups.html
	reset-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html
    """

    write_parameter("redshift", "modify-cluster-parameter-group")