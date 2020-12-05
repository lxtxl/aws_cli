#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-nodegroup-config.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-name : The name of the Amazon EKS cluster that the managed node group resides in.
    # nodegroup-name : The name of the managed node group to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("eks", "update-nodegroup-config", "cluster-name", "nodegroup-name", add_option_dict)
