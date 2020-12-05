#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/create-schema.html
	describe-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-schema.html
	export-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/export-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-schemas.html
	search-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/search-schemas.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-schema.html
    """

    write_parameter("schemas", "delete-schema")