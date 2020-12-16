#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/create-ledger.html
	delete-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/delete-ledger.html
	describe-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-ledger.html
	list-ledgers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-ledgers.html
    """

    write_parameter("qldb", "update-ledger")