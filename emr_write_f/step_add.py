#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/cancel-steps.html
	describe-step : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html
	list-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-steps.html
    """

    write_parameter("emr", "add-steps")