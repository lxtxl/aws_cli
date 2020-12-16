#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/list-s3-resources.html
if __name__ == '__main__':
    """
	associate-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/associate-s3-resources.html
	disassociate-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/disassociate-s3-resources.html
	update-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/update-s3-resources.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("macie", "list-s3-resources", add_option_dict)