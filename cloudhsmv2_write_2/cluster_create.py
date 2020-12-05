#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/create-cluster.html
if __name__ == '__main__':
    """
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/delete-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-clusters.html
	initialize-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/initialize-cluster.html
    """

    parameter_display_string = """
    # subnet-ids : The identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:

All subnets must be in the same virtual private cloud (VPC).
You can specify only one subnet per Availability Zone.

(string)
    # hsm-type : The type of HSM to use in the cluster. Currently the only allowed value is hsm1.medium .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsmv2", "create-cluster", "subnet-ids", "hsm-type", add_option_dict)
