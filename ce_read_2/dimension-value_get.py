#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-dimension-values.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # time-period : 
    # dimension : The name of the dimension. Each Dimension is available for a different Context . For more information, see Context .
Possible values:

AZ
INSTANCE_TYPE
LINKED_ACCOUNT
LINKED_ACCOUNT_NAME
OPERATION
PURCHASE_TYPE
REGION
SERVICE
SERVICE_CODE
USAGE_TYPE
USAGE_TYPE_GROUP
RECORD_TYPE
OPERATING_SYSTEM
TENANCY
SCOPE
PLATFORM
SUBSCRIPTION_ID
LEGAL_ENTITY_NAME
DEPLOYMENT_OPTION
DATABASE_ENGINE
CACHE_ENGINE
INSTANCE_TYPE_FAMILY
BILLING_ENTITY
RESERVATION_ID
RESOURCE_ID
RIGHTSIZING_TYPE
SAVINGS_PLANS_TYPE
SAVINGS_PLAN_ARN
PAYMENT_OPTION
    """

    execute_two_parameter("ce", "get-dimension-values", "time-period", "dimension", parameter_display_string)