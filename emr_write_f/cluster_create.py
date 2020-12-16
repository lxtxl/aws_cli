#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-clusters.html
	modify-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-cluster.html
	terminate-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/terminate-clusters.html
    """

    write_parameter("emr", "create-cluster")