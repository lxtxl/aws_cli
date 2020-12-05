#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-instance-groups.html
if __name__ == '__main__':
    """
	modify-instance-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-groups.html
    """

    parameter_display_string = """
    # cluster-id : A unique string that identifies a cluster. The create-cluster command returns this identifier. You can use the list-clusters command to get cluster IDs.
    # instance-groups  ... : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "add-instance-groups", "cluster-id", "instance-groups  ...", add_option_dict)
