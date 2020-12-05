#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-configuration-revision.html
if __name__ == '__main__':
    """
	list-configuration-revisions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-configuration-revisions.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.
    # revision : 
    """

    execute_two_parameter("kafka", "describe-configuration-revision", "arn", "revision", parameter_display_string)