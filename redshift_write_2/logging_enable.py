#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-logging.html
if __name__ == '__main__':
    """
	disable-logging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-logging.html
    """

    parameter_display_string = """
    # cluster-identifier : The identifier of the cluster on which logging is to be started.
Example: examplecluster
    # bucket-name : The name of an existing S3 bucket where the log files are to be stored.
Constraints:

Must be in the same region as the cluster
The cluster must have read bucket and put object permissions
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "enable-logging", "cluster-identifier", "bucket-name", add_option_dict)
