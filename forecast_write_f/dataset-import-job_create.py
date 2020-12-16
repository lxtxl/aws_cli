#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-import-job.html
	describe-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-import-job.html
	list-dataset-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-import-jobs.html
    """

    write_parameter("forecast", "create-dataset-import-job")