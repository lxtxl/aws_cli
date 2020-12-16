#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-code-review : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-code-review.html
	list-code-reviews : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-code-reviews.html
    """

    write_parameter("codeguru-reviewer", "create-code-review")