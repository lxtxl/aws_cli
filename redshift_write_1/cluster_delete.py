#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html
	modify-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html
	pause-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/pause-cluster.html
	reboot-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html
	resize-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resize-cluster.html
	resume-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resume-cluster.html
    """

    parameter_display_string = """
    # cluster-identifier : The identifier of the cluster to be deleted.
Constraints:

Must contain lowercase characters.
Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "delete-cluster", "cluster-identifier", add_option_dict)





