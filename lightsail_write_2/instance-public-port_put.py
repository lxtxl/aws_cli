#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-instance-public-ports.html
if __name__ == '__main__':
    """
	close-instance-public-ports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/close-instance-public-ports.html
	open-instance-public-ports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/open-instance-public-ports.html
    """

    parameter_display_string = """
    # port-infos : An array of objects to describe the ports to open for the specified instance.
(structure)

Describes ports to open on an instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.
fromPort -> (integer)

The first port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - The ICMP type. For example, specify 8 as the fromPort (ICMP type), and -1 as the toPort (ICMP code), to enable ICMP Ping. For more information, see Control Messages on Wikipedia .


toPort -> (integer)

The last port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - The ICMP code. For example, specify 8 as the fromPort (ICMP type), and -1 as the toPort (ICMP code), to enable ICMP Ping. For more information, see Control Messages on Wikipedia .


protocol -> (string)

The IP protocol name.
The name can be one of the following:

tcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesnât require reliable data stream service, use UDP instead.
all - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .
udp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that donât require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
icmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify icmp as the protocol , you must specify the ICMP type using the fromPort parameter, and ICMP code using the toPort parameter.


cidrs -> (list)

The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.
Examples:

To allow the IP address 192.0.2.44 , specify 192.0.2.44 or 192.0.2.44/32 .
To allow the IP addresses 192.0.2.0 to 192.0.2.255 , specify 192.0.2.0/24 .

For more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .
(string)

cidrListAliases -> (list)

An alias that defines access for a preconfigured range of IP addresses.
The only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.
(string)
    # instance-name : The name of the instance for which to open ports.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "put-instance-public-ports", "port-infos", "instance-name", add_option_dict)
