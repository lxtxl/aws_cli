#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-job-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-definitions.html
	register-job-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html
    """

    write_parameter("batch", "deregister-job-definition")