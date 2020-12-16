#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-build-batches.html
if __name__ == '__main__':
    """
	delete-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-build-batch.html
	retry-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/retry-build-batch.html
	start-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-build-batch.html
	stop-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build-batch.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("codebuild", "list-build-batches", add_option_dict)