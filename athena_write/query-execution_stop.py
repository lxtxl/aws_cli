#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-query-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-execution.html
	list-query-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-query-executions.html
	start-query-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html
    """

    write_parameter("athena", "stop-query-execution")