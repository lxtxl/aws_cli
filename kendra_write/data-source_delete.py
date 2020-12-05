#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-data-source.html
	describe-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html
    """

    write_parameter("kendra", "delete-data-source")