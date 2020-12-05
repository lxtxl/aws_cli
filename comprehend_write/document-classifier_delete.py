#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-document-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-document-classifier.html
	describe-document-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-document-classifier.html
	list-document-classifiers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-document-classifiers.html
    """

    write_parameter("comprehend", "delete-document-classifier")