#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-account-setting.html
if __name__ == '__main__':
    """
	list-account-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-account-settings.html
	put-account-setting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/put-account-setting.html
    """

    parameter_display_string = """
    # name : The resource name for which to disable the account setting. If serviceLongArnFormat is specified, the ARN for your Amazon ECS services is affected. If taskLongArnFormat is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If containerInstanceLongArnFormat is specified, the ARN and resource ID for your Amazon ECS container instances is affected. If awsvpcTrunking is specified, the ENI limit for your Amazon ECS container instances is affected.
Possible values:

serviceLongArnFormat
taskLongArnFormat
containerInstanceLongArnFormat
awsvpcTrunking
containerInsights
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "delete-account-setting", "name", add_option_dict)





