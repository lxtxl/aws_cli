#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request.html
if __name__ == '__main__':
    """
	get-pull-request : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request.html
	list-pull-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-pull-requests.html
    """

    parameter_display_string = """
    # title : The title of the pull request. This title is used to identify the pull request to other users in the repository.
    # targets : The targets for the pull request, including the source of the code to be reviewed (the source branch) and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).
(structure)

Returns information about a target for a pull request.
repositoryName -> (string)

The name of the repository that contains the pull request.

sourceReference -> (string)

The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference -> (string)

The branch of the repository where the pull request changes are merged. Also known as the destination branch.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "create-pull-request", "title", "targets", add_option_dict)
