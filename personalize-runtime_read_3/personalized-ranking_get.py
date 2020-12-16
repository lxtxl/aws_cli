#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-runtime/get-personalized-ranking.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # campaign-arn : The Amazon Resource Name (ARN) of the campaign to use for generating the personalized ranking.
    # input-list : A list of items (by itemId ) to rank. If an item was not included in the training dataset, the item is appended to the end of the reranked list. The maximum is 500.
(string)
    """

    execute_two_parameter("personalize-runtime", "get-personalized-ranking", "campaign-arn", "input-list", parameter_display_string)