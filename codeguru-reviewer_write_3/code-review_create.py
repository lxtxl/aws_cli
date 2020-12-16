#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/create-code-review.html
if __name__ == '__main__':
    """
	describe-code-review : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-code-review.html
	list-code-reviews : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-code-reviews.html
    """

    parameter_display_string = """
    # name : The name of the code review. The name of each code review in your AWS account must be unique.
    # repository-association-arn : The Amazon Resource Name (ARN) of the ` RepositoryAssociation https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html`__ object. You can retrieve this ARN by calling ` ListRepositoryAssociations https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html`__ .
A code review can only be created on an associated repository. This is the ARN of the associated repository.
    # type : The type of report group.
Possible values:

TEST
CODE_COVERAGE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeguru-reviewer", "create-code-review", "name", "repository-association-arn", "type", add_option_dict)
