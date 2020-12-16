#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary-filter.html
	delete-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary-filter.html
	get-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary-filter.html
	list-vocabulary-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabulary-filters.html
    """

    write_parameter("transcribe", "update-vocabulary-filter")