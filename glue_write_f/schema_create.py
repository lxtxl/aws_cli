#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-schema.html
	get-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-schemas.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-schema.html
    """

    write_parameter("glue", "create-schema")