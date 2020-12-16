#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html
	modify-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html
	pause-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/pause-cluster.html
	reboot-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html
	resize-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resize-cluster.html
	resume-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resume-cluster.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("redshift", "describe-clusters", add_option_dict)