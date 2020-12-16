#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	accept-inbound-cross-cluster-search-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/accept-inbound-cross-cluster-search-connection.html
	describe-inbound-cross-cluster-search-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-inbound-cross-cluster-search-connections.html
	reject-inbound-cross-cluster-search-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/reject-inbound-cross-cluster-search-connection.html
    """

    write_parameter("es", "delete-inbound-cross-cluster-search-connection")