#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html
if __name__ == '__main__':
    """
	create-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html
	delete-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html
	get-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html
	list-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-trails.html
	update-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("cloudtrail", "describe-trails", add_option_dict)