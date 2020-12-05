#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-copy-retention-period.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-identifier : The unique identifier of the cluster for which you want to change the retention period for either automated or manual snapshots that are copied to a destination AWS Region.
Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
    # retention-period : The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region.
By default, this only changes the retention period of copied automated snapshots.
If you decrease the retention period for automated snapshots that are copied to a destination AWS Region, Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period.
Constraints: Must be at least 1 and no more than 35 for automated snapshots.
If you specify the manual option, only newly copied manual snapshots will have the new retention period.
If you specify the value of -1 newly copied manual snapshots are retained indefinitely.
Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "modify-snapshot-copy-retention-period", "cluster-identifier", "retention-period", add_option_dict)
