#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-data-source-sync-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-source-sync-jobs.html
	start-data-source-sync-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/start-data-source-sync-job.html
    """

    write_parameter("kendra", "stop-data-source-sync-job")