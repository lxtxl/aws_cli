#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-repository-association.html
if __name__ == '__main__':
    """
	list-repository-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-repository-associations.html
    """

    parameter_display_string = """
    # association-arn : The Amazon Resource Name (ARN) of the ` RepositoryAssociation https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html`__ object. You can retrieve this ARN by calling ListRepositories .
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("codeguru-reviewer", "describe-repository-association", "association-arn", add_option_dict)