#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-language-model.html
	describe-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/describe-language-model.html
	list-language-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-language-models.html
    """

    write_parameter("transcribe", "delete-language-model")