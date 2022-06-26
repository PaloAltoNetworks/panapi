#!/usr/bin/env python3

from panapi.config import PanObject

class BandwidthAllocation(PanObject):
    'A bandwidth allocation'
    _endpoint = '/sse/config/v1/bandwidth-allocations'


class IKECryptoProfile(PanObject):
    'An IKE crypto profile'
    _endpoint = '/sse/config/v1/ike-crypto-profiles'


class IKEGateway(PanObject):
    'An IKE gateway'
    _endpoint = '/sse/config/v1/ike-gateways'


class IPSedCryptoProfile(PanObject):
    'An IPSec crypto profile'
    _endpoint = '/sse/config/v1/ipsec-crypto-profiles'


class IPSecTunnel(PanObject):
    'An IPSec tunnel'
    _endpoint = '/sse/config/v1/ipsec-tunnels'


class IPSedCryptoProfile(PanObject):
    'An IPSec crypto profile'
    _endpoint = '/sse/config/v1/ipsec-crypto-profiles'


class Location(PanObject):
    'A SASE location'
    _endpoint = '/sse/config/v1/locations'


class QoSPolicyRule(PanObject):
    'A QoS policy rule'
    _endpoint = '/sse/config/v1/qos-policy-rules'


class QoSProfile(PanObject):
    'A QoS profile'
    _endpoint = '/sse/config/v1/qos-profiles'


class RemoteNetwork(PanObject):
    'A SASE remote network'
    _endpoint = '/sse/config/v1/remote-networks'


