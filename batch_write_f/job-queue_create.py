#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-job-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-job-queue.html
	describe-job-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-queues.html
	update-job-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-job-queue.html
    """

    write_parameter("batch", "create-job-queue")