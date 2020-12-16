#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-column-statistics-for-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-column-statistics-for-table.html
	update-column-statistics-for-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-column-statistics-for-table.html
    """

    write_parameter("glue", "delete-column-statistics-for-table")