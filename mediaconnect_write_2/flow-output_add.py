#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-outputs.html
if __name__ == '__main__':
    """
	remove-flow-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-output.html
	update-flow-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-output.html
    """

    parameter_display_string = """
    # flow-arn : The flow that you want to add outputs to.
    # outputs : The output that you want to add to this flow.
CidrAllowList -> (list)

The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string)

Description -> (string)

A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.

Destination -> (string)

The IP address from which video will be sent to output destinations.

Encryption -> (structure)

The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
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


MaxLatency -> (integer)

The maximum latency in milliseconds for Zixi-based streams.

Name -> (string)

The name of the output. This value must be unique within the current flow.

Port -> (integer)

The port to use when content is distributed to this output.

Protocol -> (string)

The protocol to use for the output.

RemoteId -> (string)

The remote ID for the Zixi-pull output stream.

SmoothingLatency -> (integer)

The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

StreamId -> (string)

The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.

VpcInterfaceAttachment -> (structure)

The name of the VPC interface attachment to use for this output.
VpcInterfaceName -> (string)

The name of the VPC interface to use for this output.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "add-flow-outputs", "flow-arn", "outputs", add_option_dict)
