#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/create-hsm.html
if __name__ == '__main__':
    """
	delete-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/delete-hsm.html
    """

    parameter_display_string = """
    # cluster-id : The identifier (ID) of the HSMâs cluster. To find the cluster ID, use  DescribeClusters .
    # availability-zone : The Availability Zone where you are creating the HSM. To find the clusterâs Availability Zones, use  DescribeClusters .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsmv2", "create-hsm", "cluster-id", "availability-zone", add_option_dict)
