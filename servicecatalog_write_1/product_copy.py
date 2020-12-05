#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/copy-product.html
if __name__ == '__main__':
    """
	create-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html
	delete-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-product.html
	describe-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product.html
	provision-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html
	search-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-products.html
	update-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-product.html
    """

    parameter_display_string = """
    # source-product-arn : The Amazon Resource Name (ARN) of the source product.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "copy-product", "source-product-arn", add_option_dict)





