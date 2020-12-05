#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-cluster-settings.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster : The name of the cluster to modify the settings for.
    # settings : The setting to use by default for a cluster. This parameter is used to enable CloudWatch Container Insights for a cluster. If this value is specified, it will override the containerInsights value set with  PutAccountSetting or  PutAccountSettingDefault .
(structure)

The settings to use when creating a cluster. This parameter is used to enable CloudWatch Container Insights for a cluster.
name -> (string)

The name of the cluster setting. The only supported value is containerInsights .

value -> (string)

The value to set for the cluster setting. The supported values are enabled and disabled . If enabled is specified, CloudWatch Container Insights will be enabled for the cluster, otherwise it will be disabled unless the containerInsights account setting is enabled. If a cluster value is specified, it will override the containerInsights value set with  PutAccountSetting or  PutAccountSettingDefault .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecs", "update-cluster-settings", "cluster", "settings", add_option_dict)
