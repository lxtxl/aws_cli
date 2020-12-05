#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-policies.html
if __name__ == '__main__':
    """
	delete-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/delete-scaling-policy.html
	put-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scaling-policy.html
    """

    parameter_display_string = """
    # service-namespace : The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.
Possible values:

ecs
elasticmapreduce
ec2
appstream
dynamodb
rds
sagemaker
custom-resource
comprehend
lambda
cassandra
kafka
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

    execute_one_parameter("application-autoscaling", "describe-scaling-policies", "service-namespace", add_option_dict)