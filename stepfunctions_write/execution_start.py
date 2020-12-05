#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-execution.html
	list-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-executions.html
	stop-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/stop-execution.html
    """

    write_parameter("stepfunctions", "start-execution")