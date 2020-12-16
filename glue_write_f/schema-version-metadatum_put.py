#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	query-schema-version-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/query-schema-version-metadata.html
	remove-schema-version-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/remove-schema-version-metadata.html
    """

    write_parameter("glue", "put-schema-version-metadata")