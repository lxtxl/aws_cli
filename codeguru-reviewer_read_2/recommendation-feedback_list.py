#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-recommendation-feedback.html
if __name__ == '__main__':
    """
	list-recommendation-feedback : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-recommendation-feedback.html
	put-recommendation-feedback : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/put-recommendation-feedback.html
    """

    parameter_display_string = """
    # code-review-arn : The Amazon Resource Name (ARN) of the ` CodeReview https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html`__ object.
    # recommendation-id : The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.
    """

    execute_two_parameter("codeguru-reviewer", "describe-recommendation-feedback", "code-review-arn", "recommendation-id", parameter_display_string)