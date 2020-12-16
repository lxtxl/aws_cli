#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	activate-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/activate-pipeline.html
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/create-pipeline.html
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/delete-pipeline.html
	describe-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-pipelines.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-pipelines.html
    """

    write_parameter("datapipeline", "deactivate-pipeline")