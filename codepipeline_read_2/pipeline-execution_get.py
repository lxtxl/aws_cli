#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-execution.html
if __name__ == '__main__':
    """
	list-pipeline-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipeline-executions.html
	start-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html
	stop-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/stop-pipeline-execution.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline about which you want to get execution details.
    # pipeline-execution-id : The ID of the pipeline execution about which you want to get execution details.
    """

    execute_two_parameter("codepipeline", "get-pipeline-execution", "pipeline-name", "pipeline-execution-id", parameter_display_string)