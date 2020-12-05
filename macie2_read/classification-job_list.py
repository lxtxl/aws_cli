#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-classification-jobs.html
if __name__ == '__main__':
    """
	create-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-classification-job.html
	describe-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-classification-job.html
	update-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-classification-job.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("macie2", "list-classification-jobs", add_option_dict)