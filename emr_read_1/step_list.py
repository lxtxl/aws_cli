#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-steps.html
if __name__ == '__main__':
    """
	add-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-steps.html
	cancel-steps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/cancel-steps.html
	describe-step : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html
    """

    parameter_display_string = """
    # cluster-id : The identifier of the cluster for which to list the steps.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("emr", "list-steps", "cluster-id", add_option_dict)