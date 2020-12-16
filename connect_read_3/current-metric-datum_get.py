#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-current-metric-data.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # filters : An array of objects that describe a filter that returns a more specific list of instance recommendations.
(structure)

Describes a filter that returns a more specific list of recommendations.
This filter is used with the GetAutoScalingGroupRecommendations and GetEC2InstanceRecommendations actions.
name -> (string)

The name of the filter.
Specify Finding to return recommendations with a specific finding classification (e.g., Overprovisioned ).
Specify RecommendationSourceType to return recommendations of a specific resource type (e.g., AutoScalingGroup ).

values -> (list)

The value of the filter.
The valid values for this parameter are as follows, depending on what you specify for the name parameter and the resource type that you wish to filter results for:

Specify Optimized or NotOptimized if you specified the name parameter as Finding and you want to filter results for Auto Scaling groups.
Specify Underprovisioned , Overprovisioned , or Optimized if you specified the name parameter as Finding and you want to filter results for EC2 instances.
Specify Ec2Instance or AutoScalingGroup if you specified the name parameter as RecommendationSourceType .

(string)
    """

    execute_two_parameter("connect", "get-current-metric-data", "instance-id", "filters", parameter_display_string)