#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task-assessment-run.html
	describe-replication-task-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-task-assessment-runs.html
	start-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task-assessment-run.html
    """

    write_parameter("dms", "cancel-replication-task-assessment-run")