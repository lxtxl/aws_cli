#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/start-bulk-deployment.html
if __name__ == '__main__':
    """
	list-bulk-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-bulk-deployments.html
	stop-bulk-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/stop-bulk-deployment.html
    """

    parameter_display_string = """
    # execution-role-arn : The ARN of the execution role to associate with the bulk deployment operation. This IAM role must allow the ââgreengrass:CreateDeploymentââ action for all group versions that are listed in the input file. This IAM role must have access to the S3 bucket containing the input file.
    # input-file-uri : The URI of the input file contained in the S3 bucket. The execution role must have ââgetObjectââ permissions on this bucket to access the input file. The input file is a JSON-serialized, line delimited file with UTF-8 encoding that provides a list of group and version IDs and the deployment type. This file must be less than 100 MB. Currently, AWS IoT Greengrass supports only ââNewDeploymentââ deployment types.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("greengrass", "start-bulk-deployment", "execution-role-arn", "input-file-uri", add_option_dict)
