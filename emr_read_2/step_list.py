#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html
if __name__ == '__main__':
    """
	add-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-steps.html
	cancel-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/cancel-steps.html
	list-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-steps.html
    """

    parameter_display_string = """
    # cluster-id : The identifier of the cluster with steps to describe.
    # step-id : The identifier of the step to describe.
    """

    execute_two_parameter("emr", "describe-step", "cluster-id", "step-id", parameter_display_string)