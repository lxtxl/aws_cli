#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/promote-read-replica-db-cluster.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-cluster-identifier : The identifier of the DB cluster read replica to promote. This parameter isnât case-sensitive.
Constraints:

Must match the identifier of an existing DB cluster read replica.

Example: my-cluster-replica1
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "promote-read-replica-db-cluster", "db-cluster-identifier", add_option_dict)





