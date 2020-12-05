#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/disable-hbase-backups.html
if __name__ == '__main__':
    """
	create-hbase-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-hbase-backup.html
	schedule-hbase-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/schedule-hbase-backup.html
    """

    parameter_display_string = """
    # cluster-id : A unique string that identifies a cluster. The create-cluster command returns this identifier. You can use the list-clusters command to get cluster IDs.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("emr", "disable-hbase-backups", "cluster-id", add_option_dict)





