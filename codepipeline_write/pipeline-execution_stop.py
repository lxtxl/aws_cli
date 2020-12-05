#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-execution.html
	list-pipeline-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipeline-executions.html
	start-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html
    """

    write_parameter("codepipeline", "stop-pipeline-execution")