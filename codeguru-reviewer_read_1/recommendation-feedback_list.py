#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-recommendation-feedback.html
if __name__ == '__main__':
    """
	describe-recommendation-feedback : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-recommendation-feedback.html
	put-recommendation-feedback : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/put-recommendation-feedback.html
    """

    parameter_display_string = """
    # code-review-arn : The Amazon Resource Name (ARN) of the ` CodeReview https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html`__ object.
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

    execute_one_parameter("codeguru-reviewer", "list-recommendation-feedback", "code-review-arn", add_option_dict)