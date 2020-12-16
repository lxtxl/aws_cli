#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-configuration-profile.html
if __name__ == '__main__':
    """
	delete-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-configuration-profile.html
	get-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration-profile.html
	list-configuration-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-configuration-profiles.html
	update-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-configuration-profile.html
    """

    parameter_display_string = """
    # application-id : The application ID.
    # name : A name for the configuration profile.
    # location-uri : A URI to locate the configuration. You can specify a Systems Manager (SSM) document, an SSM Parameter Store parameter, or an Amazon S3 object. For an SSM document, specify either the document name in the format ssm-document://<Document_name> or the Amazon Resource Name (ARN). For a parameter, specify either the parameter name in the format ssm-parameter://<Parameter_name> or the ARN. For an Amazon S3 object, specify the URI in the following format: s3://<bucket>/<objectKey> . Here is an example: s3://my-bucket/my-app/us-east-1/my-config.json
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appconfig", "create-configuration-profile", "application-id", "name", "location-uri", add_option_dict)
