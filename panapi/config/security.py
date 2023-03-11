#!/usr/bin/env python3

from panapi.config import PanObject


class AntiSpywareProfile(PanObject):
    "An anti-spyware profile"
    _endpoint = "/sse/config/v1/anti-spyware-profiles"


class AntiSpywareSignature(PanObject):
    "An anti-spyware signature"
    _endpoint = "/sse/config/v1/anti-spyware-signature"


class DNSSecurityProfile(PanObject):
    "A DNS security profile"
    _endpoint = "/sse/config/v1/dns-security-profiles"


class DecryptionExclusion(PanObject):
    "A decryption exclusion"
    _endpoint = "/sse/config/v1/decryption-exclusions"


class DecryptionProfile(PanObject):
    "A decryption profile"
    _endpoint = "/sse/config/v1/decryption-profiles"


class DecryptionRule(PanObject):
    "A decryption rule"
    _endpoint = "/sse/config/v1/decryption-rules"


class FileBlockingProfile(PanObject):
    "A file blocking profile"
    _endpoint = "/sse/config/v1/file-blocking-profiles"


class HTTPHeaderProfile(PanObject):
    "An HTTP header profile"
    _endpoint = "/sse/config/v1/http-header-profiles"


class ProfileGroup(PanObject):
    "A profile group"
    _endpoint = "/sse/config/v1/profile-groups"


class SecurityRule(PanObject):
    "A security rule"
    _endpoint = "/sse/config/v1/security-rules"


class URLAccessProfile(PanObject):
    "A URL access profile"
    _endpoint = "/sse/config/v1/url-access-profiles"


class VulnerabilityProtectionProfile(PanObject):
    "A vulnerability protection profile"
    _endpoint = "/sse/config/v1/vulnerability-protection-profiles"


class VulnerabilityProtectionSignature(PanObject):
    "A vulnerability protection signature"
    _endpoint = "/sse/config/v1/vulnerability-protection-signatures"


class WildFireAntivirusProfile(PanObject):
    "A WildFire antivirus profile"
    _endpoint = "/sse/config/v1/wildfire-antivirus-profiles"
