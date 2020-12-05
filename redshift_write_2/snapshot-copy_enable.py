#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-snapshot-copy.html
if __name__ == '__main__':
    """
	disable-snapshot-copy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-snapshot-copy.html
    """

    parameter_display_string = """
    # cluster-identifier : The unique identifier of the source cluster to copy snapshots from.
Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.
    # destination-region : The destination AWS Region that you want to copy snapshots to.
Constraints: Must be the name of a valid AWS Region. For more information, see Regions and Endpoints in the Amazon Web Services General Reference.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "enable-snapshot-copy", "cluster-identifier", "destination-region", add_option_dict)
