#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-elasticsearch-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-elasticsearch-domain.html
	describe-elasticsearch-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain.html
	describe-elasticsearch-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domains.html
	upgrade-elasticsearch-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/upgrade-elasticsearch-domain.html
    """

    write_parameter("es", "create-elasticsearch-domain")