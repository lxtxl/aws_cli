#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-pipeline-execution.html
	list-pipeline-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-pipeline-executions.html
	start-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-pipeline-execution.html
	stop-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-pipeline-execution.html
    """

    write_parameter("sagemaker", "update-pipeline-execution")