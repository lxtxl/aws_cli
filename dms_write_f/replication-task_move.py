#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-task.html
	delete-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task.html
	describe-replication-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-tasks.html
	modify-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-task.html
	start-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task.html
	stop-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html
    """

    write_parameter("dms", "move-replication-task")