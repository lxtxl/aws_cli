#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-snapshot.html
if __name__ == '__main__':
    """
	copy-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/copy-cluster-snapshot.html
	create-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-snapshot.html
	describe-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html
	modify-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html
    """

    parameter_display_string = """
    # snapshot-identifier : The unique identifier of the manual snapshot to be deleted.
Constraints: Must be the name of an existing snapshot that is in the available , failed , or cancelled state.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "delete-cluster-snapshot", "snapshot-identifier", add_option_dict)





