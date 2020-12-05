#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-mailbox-export-job.html
	list-mailbox-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-export-jobs.html
	start-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/start-mailbox-export-job.html
    """

    write_parameter("workmail", "cancel-mailbox-export-job")