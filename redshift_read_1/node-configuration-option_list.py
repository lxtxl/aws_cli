#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-node-configuration-options.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # action-type : The action type to evaluate for possible node configurations. Specify ârestore-clusterâ to get configuration combinations based on an existing snapshot. Specify ârecommend-node-configâ to get configuration recommendations based on an existing cluster or snapshot. Specify âresize-clusterâ to get configuration combinations for elastic resize based on an existing cluster.
Possible values:

restore-cluster
recommend-node-config
resize-cluster
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("redshift", "describe-node-configuration-options", "action-type", add_option_dict)