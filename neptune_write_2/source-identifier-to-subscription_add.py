#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/add-source-identifier-to-subscription.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # subscription-name : The name of the event notification subscription you want to add a source identifier to.
    # source-identifier : The identifier of the event source to be added.
Constraints:

If the source type is a DB instance, then a DBInstanceIdentifier must be supplied.
If the source type is a DB security group, a DBSecurityGroupName must be supplied.
If the source type is a DB parameter group, a DBParameterGroupName must be supplied.
If the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("neptune", "add-source-identifier-to-subscription", "subscription-name", "source-identifier", add_option_dict)
