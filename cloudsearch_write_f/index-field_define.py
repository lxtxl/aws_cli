#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-index-field : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-index-field.html
	describe-index-fields : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-index-fields.html
    """

    write_parameter("cloudsearch", "define-index-field")