#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/cancel-steps.html
if __name__ == '__main__':
    """
	add-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-steps.html
	describe-step : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html
	list-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-steps.html
    """

    parameter_display_string = """
    # cluster-id : The ClusterID for which specified steps will be canceled. Use  RunJobFlow and  ListClusters to get ClusterIDs.
    # step-ids : The list of StepIDs to cancel. Use  ListSteps to get steps and their states for the specified cluster.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "cancel-steps", "cluster-id", "step-ids", add_option_dict)
