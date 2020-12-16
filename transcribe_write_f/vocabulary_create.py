#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary.html
	get-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary.html
	list-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabularies.html
	update-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-vocabulary.html
    """

    write_parameter("transcribe", "create-vocabulary")