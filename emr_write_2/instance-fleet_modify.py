#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-fleet.html
if __name__ == '__main__':
    """
	add-instance-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-instance-fleet.html
	list-instance-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-instance-fleets.html
    """

    parameter_display_string = """
    # cluster-id : The unique identifier of the cluster.
    # instance-fleet : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "modify-instance-fleet", "cluster-id", "instance-fleet", add_option_dict)
