#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-schema.html
	describe-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-schemas.html
    """

    write_parameter("personalize", "delete-schema")