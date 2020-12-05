#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-constraint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-constraint.html
	delete-constraint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-constraint.html
	describe-constraint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-constraint.html
    """

    write_parameter("servicecatalog", "update-constraint")