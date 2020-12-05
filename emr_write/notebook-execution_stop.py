#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-notebook-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-notebook-execution.html
	list-notebook-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-notebook-executions.html
	start-notebook-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/start-notebook-execution.html
    """

    write_parameter("emr", "stop-notebook-execution")