#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-provisioned-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product.html
	scan-provisioned-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/scan-provisioned-products.html
	search-provisioned-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-provisioned-products.html
	terminate-provisioned-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/terminate-provisioned-product.html
    """

    write_parameter("servicecatalog", "update-provisioned-product")