#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	build-suggesters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/build-suggesters.html
	define-suggester : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/define-suggester.html
	describe-suggesters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-suggesters.html
    """

    write_parameter("cloudsearch", "delete-suggester")