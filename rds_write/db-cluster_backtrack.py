#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster.html
	describe-db-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html
	failover-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/failover-db-cluster.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-cluster.html
	stop-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html
    """

    write_parameter("rds", "backtrack-db-cluster")