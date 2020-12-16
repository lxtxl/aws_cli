#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workteam.html
if __name__ == '__main__':
    """
	delete-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-workteam.html
	describe-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-workteam.html
	list-workteams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workteams.html
	update-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-workteam.html
    """

    parameter_display_string = """
    # workteam-name : The name of the work team. Use this name to identify the work team.
    # member-definitions : A list of MemberDefinition objects that contains objects that identify the workers that make up the work team.
Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use CognitoMemberDefinition . For workforces created using your own OIDC identity provider (IdP) use OidcMemberDefinition . Do not provide input for both of these parameters in a single request.
For workforces created using Amazon Cognito, private work teams correspond to Amazon Cognito user groups within the user pool used to create a workforce. All of the CognitoMemberDefinition objects that make up the member definition must have the same ClientId and UserPool values. To add a Amazon Cognito user group to an existing worker pool, see Adding groups to a User Pool . For more information about user pools, see `Amazon Cognito User Pools .
For workforces created using your own OIDC IdP, specify the user groups that you want to include in your private work team in OidcMemberDefinition by listing those groups in Groups .
(structure)

Defines an Amazon Cognito or your own OIDC IdP user group that is part of a work team.
CognitoMemberDefinition -> (structure)

The Amazon Cognito user group that is part of the work team.
UserPool -> (string)

An identifier for a user pool. The user pool must be in the same region as the service that you are calling.

UserGroup -> (string)

An identifier for a user group.

ClientId -> (string)

An identifier for an application client. You must create the app client ID using Amazon Cognito.


OidcMemberDefinition -> (structure)

A list user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of Groups , you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.
Groups -> (list)

A list of comma seperated strings that identifies user groups in your OIDC IdP. Each user group is made up of a group of private workers.
(string)
    # description : A description of the work team.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker", "create-workteam", "workteam-name", "member-definitions", "description", add_option_dict)
