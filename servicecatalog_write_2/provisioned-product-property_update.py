#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioned-product-properties.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # provisioned-product-id : The identifier of the provisioned product.
    # provisioned-product-properties : A map that contains the provisioned product properties to be updated.
The LAUNCH_ROLE key accepts role ARNs. This key allows an administrator to call UpdateProvisionedProductProperties to update the launch role that is associated with a provisioned product. This role is used when an end user calls a provisioning operation such as UpdateProvisionedProduct , TerminateProvisionedProduct , or ExecuteProvisionedProductServiceAction . Only a role ARN or an empty string "" is valid. A user ARN is invalid. if an admin user passes an empty string "" as the value for the key LAUNCH_ROLE , the admin removes the launch role that is associated with the provisioned product. As a result, the end user operations use the credentials of the end user.
The OWNER key accepts user ARNs and role ARNs. The owner is the user that has permission to see, update, terminate, and execute service actions in the provisioned product.
The administrator can change the owner of a provisioned product to another IAM user within the same account. Both end user owners and administrators can see ownership history of the provisioned product using the ListRecordHistory API. The new owner can describe all past records for the provisioned product using the DescribeRecord API. The previous owner can no longer use DescribeRecord , but can still see the productâs history from when he was an owner using ListRecordHistory .
If a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or Service Catalog console such as update, terminate, and execute service actions. If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through API or the Service Catalog console on that provisioned product.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "update-provisioned-product-properties", "provisioned-product-id", "provisioned-product-properties", add_option_dict)
