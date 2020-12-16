#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-utterances-view.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # bot-name : The name of the bot for which utterance information should be returned.
    # bot-versions : An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.
(string)
    """

    execute_two_parameter("lex-models", "get-utterances-view", "bot-name", "bot-versions", parameter_display_string)