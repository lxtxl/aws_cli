#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-findings-filter.html
	get-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-findings-filter.html
	list-findings-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-findings-filters.html
	update-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-findings-filter.html
    """

    write_parameter("macie2", "create-findings-filter")