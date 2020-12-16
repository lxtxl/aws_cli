#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-custom-data-identifier.html
	get-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-custom-data-identifier.html
	list-custom-data-identifiers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-custom-data-identifiers.html
	test-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/test-custom-data-identifier.html
    """

    write_parameter("macie2", "delete-custom-data-identifier")