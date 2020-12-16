#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-human-loop : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/delete-human-loop.html
	describe-human-loop : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/describe-human-loop.html
	list-human-loops : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/list-human-loops.html
	stop-human-loop : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/stop-human-loop.html
    """

    write_parameter("sagemaker-a2i-runtime", "start-human-loop")