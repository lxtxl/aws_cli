#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/register-type.html
if __name__ == '__main__':
    """
	deregister-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deregister-type.html
	describe-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-type.html
	list-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-types.html
    """

    parameter_display_string = """
    # type-name : The name of the type being registered.
We recommend that type names adhere to the following pattern: company_or_organization ::service ::type .

Note
The following organization namespaces are reserved and cannot be used in your resource type names:

Alexa
AMZN
Amazon
AWS
Custom
Dev
    # schema-handler-package : A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.
For information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide .

Note
As part of registering a resource provider type, CloudFormation must be able to access the S3 bucket which contains the schema handler package for that resource provider. For more information, see IAM Permissions for Registering a Resource Provider in the AWS CloudFormation User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "register-type", "type-name", "schema-handler-package", add_option_dict)
