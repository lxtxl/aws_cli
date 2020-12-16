#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-data-set.html
	delete-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-data-set.html
	get-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-data-set.html
	list-data-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-data-sets.html
    """

    write_parameter("dataexchange", "update-data-set")