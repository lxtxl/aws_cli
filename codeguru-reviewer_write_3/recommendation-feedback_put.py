#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/put-recommendation-feedback.html
if __name__ == '__main__':
    """
	describe-recommendation-feedback : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-recommendation-feedback.html
	list-recommendation-feedback : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-recommendation-feedback.html
    """

    parameter_display_string = """
    # code-review-arn : The Amazon Resource Name (ARN) of the ` CodeReview https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html`__ object.
    # recommendation-id : The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.
    # reactions : List for storing reactions. Reactions are utf-8 text code for emojis. If you send an empty list it clears all your feedback.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeguru-reviewer", "put-recommendation-feedback", "code-review-arn", "recommendation-id", "reactions", add_option_dict)
