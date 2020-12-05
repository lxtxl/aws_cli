#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-file-upload-url.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # assignment-id : The ID of the assignment that contains the question with a FileUploadAnswer.
    # question-identifier : The identifier of the question with a FileUploadAnswer, as specified in the QuestionForm of the HIT.
    """

    execute_two_parameter("mturk", "get-file-upload-url", "assignment-id", "question-identifier", parameter_display_string)