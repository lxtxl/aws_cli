#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html
if __name__ == '__main__':
    """
	delete-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-compute-environment.html
	describe-compute-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-compute-environments.html
	update-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html
    """

    parameter_display_string = """
    # compute-environment-name : The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    # type : The type of the compute environment: MANAGED or UNMANAGED . For more information, see Compute Environments in the AWS Batch User Guide .
Possible values:

MANAGED
UNMANAGED
    # service-role : The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.

Note
Depending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesnât use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("batch", "create-compute-environment", "compute-environment-name", "type", "service-role", add_option_dict)
