#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-revision.html
	get-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-revision.html
	update-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-revision.html
    """

    write_parameter("dataexchange", "create-revision")