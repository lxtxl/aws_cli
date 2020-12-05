#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-snapshot-copy.html
if __name__ == '__main__':
    """
	enable-snapshot-copy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-snapshot-copy.html
    """

    parameter_display_string = """
    # cluster-identifier : The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.
Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "disable-snapshot-copy", "cluster-identifier", add_option_dict)





