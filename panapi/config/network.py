#!/usr/bin/env python3

from panapi.config import PanObject


class BandwidthAllocation(PanObject):
    "A bandwidth allocation"
    _endpoint = "/sse/config/v1/bandwidth-allocations"


class IKECryptoProfile(PanObject):
    "An IKE crypto profile"
    _endpoint = "/sse/config/v1/ike-crypto-profiles"


class IKEGateway(PanObject):
    "An IKE gateway"
    _endpoint = "/sse/config/v1/ike-gateways"


class IPSecCryptoProfile(PanObject):
    "An IPSec crypto profile"
    _endpoint = "/sse/config/v1/ipsec-crypto-profiles"


class IPSecTunnel(PanObject):
    "An IPSec tunnel"
    _endpoint = "/sse/config/v1/ipsec-tunnels"


class Location(PanObject):
    "A SASE location"
    _endpoint = "/sse/config/v1/locations"
    # TODO Remove this once ADI-13944 is fixed
    folder = "Shared"
    name = "dummy"

    def list(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint
        params = {"folder": self.folder}
        try:
            session.response = session.get(url=url, params=params)
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 200:
                result = session.response.json()
                return result


class QoSPolicyRule(PanObject):
    "A QoS policy rule"
    _endpoint = "/sse/config/v1/qos-policy-rules"


class QoSProfile(PanObject):
    "A QoS profile"
    _endpoint = "/sse/config/v1/qos-profiles"


class RemoteNetwork(PanObject):
    "A SASE remote network"
    _endpoint = "/sse/config/v1/remote-networks"


class SharedInfrastructureSetting(PanObject):
    "Shared Infrastructure Settings"
    _endpoint = "/sse/config/v1/shared-infrastructure-settings"
    # TODO Fix this!
    folder = "Shared"
    name = "dummy"

    def list(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint
        params = {"folder": self.folder}
        try:
            session.response = session.get(url=url, params=params)
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 200:
                result = session.response.json()
                return result


class ServiceConnection(PanObject):
    "Service Connections"
    _endpoint = "/sse/config/v1/service-connections"


class InternalDNSServer(PanObject):
    "Internal DNS Servers"
    _endpoint = "/sse/config/v1/ingternal-dns-servers"


class TrafficSteeringRule(PanObject):
    "Traffic steering rules"
    _endpoint = "/sse/config/v1/traffic-steering-rules"
