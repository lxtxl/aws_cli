#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster.html
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster.html
	describe-db-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-clusters.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/start-db-cluster.html
	stop-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/stop-db-cluster.html
    """

    write_parameter("neptune", "failover-db-cluster")