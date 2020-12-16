#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-pipeline-execution.html
if __name__ == '__main__':
    """
	describe-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-pipeline-execution.html
	list-pipeline-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-pipeline-executions.html
	start-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-pipeline-execution.html
	stop-pipeline-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-pipeline-execution.html
    """

    parameter_display_string = """
    # pipeline-execution-arn : The Amazon Resource Name (ARN) of the pipeline execution.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "update-pipeline-execution", "pipeline-execution-arn", add_option_dict)





