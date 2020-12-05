#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html
if __name__ == '__main__':
    """
	delete-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-instance.html
	describe-replication-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-instances.html
	modify-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-instance.html
	reboot-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reboot-replication-instance.html
    """

    parameter_display_string = """
    # replication-instance-identifier : The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain 1-63 alphanumeric characters or hyphens.
First character must be a letter.
Canât end with a hyphen or contain two consecutive hyphens.

Example: myrepinstance
    # replication-instance-class : The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to "dms.c4.large" .
For more information on the settings and capacities for the available replication instance classes, see Selecting the right AWS DMS replication instance for your migration .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "create-replication-instance", "replication-instance-identifier", "replication-instance-class", add_option_dict)
