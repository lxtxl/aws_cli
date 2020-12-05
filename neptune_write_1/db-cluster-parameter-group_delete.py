#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-cluster-parameter-group.html
	create-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster-parameter-group.html
	describe-db-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-cluster-parameter-groups.html
	modify-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-cluster-parameter-group.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reset-db-cluster-parameter-group.html
    """

    parameter_display_string = """
    # db-cluster-parameter-group-name : The name of the DB cluster parameter group.
Constraints:

Must be the name of an existing DB cluster parameter group.
You canât delete a default DB cluster parameter group.
Cannot be associated with any DB clusters.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("neptune", "delete-db-cluster-parameter-group", "db-cluster-parameter-group-name", add_option_dict)





