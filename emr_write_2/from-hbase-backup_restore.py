#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/restore-from-hbase-backup.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-id : A unique string that identifies a cluster. The create-cluster command returns this identifier. You can use the list-clusters command to get cluster IDs.
    # dir : The Amazon S3 location of the Hbase backup. Example: s3://mybucket/mybackup , where mybucket is the specified Amazon S3 bucket and mybackup is the specified backup location. The path argument must begin with s3://, which refers to an Amazon S3 bucket.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "restore-from-hbase-backup", "cluster-id", "dir", add_option_dict)
