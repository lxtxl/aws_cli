#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html
	delete-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-data-catalog.html
	get-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-data-catalog.html
	list-data-catalogs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-data-catalogs.html
    """

    write_parameter("athena", "update-data-catalog")