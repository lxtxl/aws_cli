#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html
if __name__ == '__main__':
    """
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-clusters.html
	modify-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-cluster.html
	terminate-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/terminate-clusters.html
    """

    parameter_display_string = """
    # release-label    | --ami-version : 
    # instance-fleets  | --instance-groups  | --instance-type  --instance-count : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "create-cluster", "release-label    | --ami-version", "instance-fleets  | --instance-groups  | --instance-type  --instance-count", add_option_dict)
