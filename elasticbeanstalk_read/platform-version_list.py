#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-platform-version.html
if __name__ == '__main__':
    """
	create-platform-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-platform-version.html
	delete-platform-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-platform-version.html
	list-platform-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-versions.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("elasticbeanstalk", "describe-platform-version", add_option_dict)