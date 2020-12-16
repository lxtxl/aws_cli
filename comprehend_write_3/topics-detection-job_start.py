#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-topics-detection-job.html
if __name__ == '__main__':
    """
	describe-topics-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-topics-detection-job.html
	list-topics-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-topics-detection-jobs.html
    """

    parameter_display_string = """
    # input-data-config : 
    # output-data-config : 
    # data-access-role-arn : The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("comprehend", "start-topics-detection-job", "input-data-config", "output-data-config", "data-access-role-arn", add_option_dict)
