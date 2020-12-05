#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/grant-flow-entitlements.html
if __name__ == '__main__':
    """
	revoke-flow-entitlement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/revoke-flow-entitlement.html
	update-flow-entitlement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-entitlement.html
    """

    parameter_display_string = """
    # entitlements : The entitlements that you want to grant on a flow.
DataTransferSubscriberFeePercent -> (integer)

Percentage from 0-100 of the data transfer cost to be billed to the subscriber.

Description -> (string)

A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.

Encryption -> (structure)

The type of encryption that will be used on the output that is associated with this entitlement.
Algorithm -> (string)

The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.

DeviceId -> (string)

The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.

KeyType -> (string)

The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).

Region -> (string)

The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.

ResourceId -> (string)

An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

RoleArn -> (string)

The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).

SecretArn -> (string)

The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.

Url -> (string)

The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementStatus -> (string)

An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you donât specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

Name -> (string)

The name of the entitlement. This value must be unique within the current flow.

Subscribers -> (list)

The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
(string)
    # flow-arn : The flow that you want to grant entitlements on.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "grant-flow-entitlements", "entitlements", "flow-arn", add_option_dict)
