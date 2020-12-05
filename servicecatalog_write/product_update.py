#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	copy-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/copy-product.html
	create-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html
	delete-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-product.html
	describe-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product.html
	provision-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html
	search-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-products.html
    """

    write_parameter("servicecatalog", "update-product")