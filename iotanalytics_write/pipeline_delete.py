#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-pipeline.html
	describe-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-pipelines.html
	update-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-pipeline.html
    """

    write_parameter("iotanalytics", "delete-pipeline")