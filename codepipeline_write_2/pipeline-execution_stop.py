#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/stop-pipeline-execution.html
if __name__ == '__main__':
    """
	get-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-execution.html
	list-pipeline-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipeline-executions.html
	start-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline to stop.
    # pipeline-execution-id : The ID of the pipeline execution to be stopped in the current stage. Use the GetPipelineState action to retrieve the current pipelineExecutionId.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codepipeline", "stop-pipeline-execution", "pipeline-name", "pipeline-execution-id", add_option_dict)
