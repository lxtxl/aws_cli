#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html
	list-lexicons : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-lexicons.html
	put-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/put-lexicon.html
    """

    write_parameter("polly", "delete-lexicon")