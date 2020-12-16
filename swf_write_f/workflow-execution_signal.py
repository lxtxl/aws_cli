#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html
	start-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html
	terminate-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/terminate-workflow-execution.html
    """

    write_parameter("swf", "signal-workflow-execution")