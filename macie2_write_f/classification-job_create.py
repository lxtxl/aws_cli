#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-classification-job.html
	list-classification-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-classification-jobs.html
	update-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-classification-job.html
    """

    write_parameter("macie2", "create-classification-job")