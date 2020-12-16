#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-tag-option.html
	describe-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-tag-option.html
	list-tag-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-tag-options.html
	update-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-tag-option.html
    """

    write_parameter("servicecatalog", "delete-tag-option")