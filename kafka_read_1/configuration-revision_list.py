#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-configuration-revisions.html
if __name__ == '__main__':
    """
	describe-configuration-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-configuration-revision.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.
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

    execute_one_parameter("kafka", "list-configuration-revisions", "arn", add_option_dict)