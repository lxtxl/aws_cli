#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio.html
	describe-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-portfolio.html
	list-portfolios : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-portfolios.html
	update-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-portfolio.html
    """

    write_parameter("servicecatalog", "create-portfolio")