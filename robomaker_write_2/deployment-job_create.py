#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-deployment-job.html
if __name__ == '__main__':
    """
	cancel-deployment-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-deployment-job.html
	describe-deployment-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-deployment-job.html
	list-deployment-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-deployment-jobs.html
	sync-deployment-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/sync-deployment-job.html
    """

    parameter_display_string = """
    # fleet : The Amazon Resource Name (ARN) of the fleet to deploy.
    # deployment-application-configs : The deployment application configuration.
(structure)

Information about a deployment application configuration.
application -> (string)

The Amazon Resource Name (ARN) of the robot application.

applicationVersion -> (string)

The version of the application.

launchConfig -> (structure)

The launch configuration.
packageName -> (string)

The package name.

preLaunchFile -> (string)

The deployment pre-launch file. This file will be executed prior to the launch file.

launchFile -> (string)

The launch file name.

postLaunchFile -> (string)

The deployment post-launch file. This file will be executed after the launch file.

environmentVariables -> (map)

An array of key/value pairs specifying environment variables for the robot application
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("robomaker", "create-deployment-job", "fleet", "deployment-application-configs", add_option_dict)
