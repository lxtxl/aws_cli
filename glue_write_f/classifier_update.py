#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-classifier.html
	delete-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-classifier.html
	get-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-classifier.html
	get-classifiers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-classifiers.html
    """

    write_parameter("glue", "update-classifier")