#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioning-artifact.html
if __name__ == '__main__':
    """
	delete-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioning-artifact.html
	describe-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html
	list-provisioning-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioning-artifacts.html
	update-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html
    """

    parameter_display_string = """
    # product-id : The product identifier.
    # parameters : The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:

LAUNCH

You are required to specify either the RoleArn or the LocalRoleName but canât use both.
Specify the RoleArn property as follows:

{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}

Specify the LocalRoleName property as follows:

{"LocalRoleName": "SCBasicLaunchRole"}

If you specify the LocalRoleName property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.

Note
The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.

You cannot have both a LAUNCH and a STACKSET constraint.
You also cannot have more than one LAUNCH constraint on a product and portfolio.

NOTIFICATION

Specify the NotificationArns property as follows:

{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}

RESOURCE_UPDATE


Specify the TagUpdatesOnProvisionedProduct property as follows:

{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}

The TagUpdatesOnProvisionedProduct property accepts a string value of ALLOWED or NOT_ALLOWED .

STACKSET

Specify the Parameters property as follows:

{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}

You cannot have both a LAUNCH and a STACKSET constraint.
You also cannot have more than one STACKSET constraint on a product and portfolio.
Products with a STACKSET constraint will launch an AWS CloudFormation stack set.

TEMPLATE

Specify the Rules property. For more information, see Template Constraint Rules .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "create-provisioning-artifact", "product-id", "parameters", add_option_dict)
