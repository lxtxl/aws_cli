#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-job.html
	describe-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/describe-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/list-jobs.html
	update-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-job.html
    """

    write_parameter("snowball", "cancel-job")