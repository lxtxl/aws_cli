#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/cancel-cluster.html
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-cluster.html
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/list-clusters.html
    """

    write_parameter("snowball", "update-cluster")