#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-database.html
	get-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-database.html
	get-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html
	update-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-database.html
    """

    write_parameter("glue", "create-database")