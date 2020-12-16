#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html
	get-workflow-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-runs.html
	start-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-workflow-run.html
	stop-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-workflow-run.html
    """

    write_parameter("glue", "resume-workflow-run")