#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/add-custom-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool where you want to add custom attributes.
    # custom-attributes : An array of custom attributes, such as Mutable and Name.
(structure)

Contains information about the schema attribute.
Name -> (string)

A schema attribute of the name type.

AttributeDataType -> (string)

The attribute data type.

DeveloperOnlyAttribute -> (boolean)


Note
We recommend that you use WriteAttributes in the user pool client to control how attributes can be mutated for new use cases instead of using DeveloperOnlyAttribute .

Specifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users will not be able to modify this attribute using their access token. For example, DeveloperOnlyAttribute can be modified using AdminUpdateUserAttributes but cannot be updated using UpdateUserAttributes.

Mutable -> (boolean)

Specifies whether the value of the attribute can be changed.
For any user pool attribute thatâs mapped to an identity provider attribute, you must set this parameter to true . Amazon Cognito updates mapped attributes when users sign in to your application through an identity provider. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see Specifying Identity Provider Attribute Mappings for Your User Pool .

Required -> (boolean)

Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

NumberAttributeConstraints -> (structure)

Specifies the constraints for an attribute of the number type.
MinValue -> (string)

The minimum value of an attribute that is of the number data type.

MaxValue -> (string)

The maximum value of an attribute that is of the number data type.


StringAttributeConstraints -> (structure)

Specifies the constraints for an attribute of the string type.
MinLength -> (string)

The minimum length.

MaxLength -> (string)

The maximum length.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "add-custom-attributes", "user-pool-id", "custom-attributes", add_option_dict)
