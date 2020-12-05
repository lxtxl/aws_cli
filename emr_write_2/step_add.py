#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-steps.html
if __name__ == '__main__':
    """
	cancel-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/cancel-steps.html
	describe-step : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html
	list-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-steps.html
    """

    parameter_display_string = """
    # cluster-id : A unique string that identifies a cluster. The create-cluster command returns this identifier. You can use the list-clusters command to get cluster IDs.
    # steps  ... : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "add-steps", "cluster-id", "steps  ...", add_option_dict)
