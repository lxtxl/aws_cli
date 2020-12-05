#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-jobs.html
	start-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/start-job.html
    """

    write_parameter("dataexchange", "cancel-job")