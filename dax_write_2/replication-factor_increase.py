#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/increase-replication-factor.html
if __name__ == '__main__':
    """
	decrease-replication-factor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/decrease-replication-factor.html
    """

    parameter_display_string = """
    # cluster-name : The name of the DAX cluster that will receive additional nodes.
    # new-replication-factor : The new number of nodes for the DAX cluster.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dax", "increase-replication-factor", "cluster-name", "new-replication-factor", add_option_dict)
