#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-schema-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-schema-version.html
	list-schema-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-schema-versions.html
	register-schema-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/register-schema-version.html
    """

    write_parameter("glue", "delete-schema-versions")