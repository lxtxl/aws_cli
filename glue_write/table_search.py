#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-table.html
	get-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table.html
	get-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-table.html
    """

    write_parameter("glue", "search-tables")