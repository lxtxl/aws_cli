#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/import-source-credentials.html
if __name__ == '__main__':
    """
	delete-source-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-source-credentials.html
	list-source-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-source-credentials.html
    """

    parameter_display_string = """
    # token : For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is the app password.
    # server-type : The source provider used for this project.
Possible values:

GITHUB
BITBUCKET
GITHUB_ENTERPRISE
    # auth-type : The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API and must be created using the AWS CodeBuild console.
Possible values:

OAUTH
BASIC_AUTH
PERSONAL_ACCESS_TOKEN
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codebuild", "import-source-credentials", "token", "server-type", "auth-type", add_option_dict)
