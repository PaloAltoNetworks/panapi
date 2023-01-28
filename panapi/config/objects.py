#!/usr/bin/env python3

from panapi.config import PanObject


class Address(PanObject):
    "An address object"
    _endpoint = "/sse/config/v1/addresses"


class AddressGroup(PanObject):
    "An address group"
    _endpoint = "/sse/config/v1/address-groups"


class Application(PanObject):
    "An application object"
    _endpoint = "/sse/config/v1/applications"


class ApplicationFilter(PanObject):
    "An application filter"
    _endpoint = "/sse/config/v1/application-filters"


class ApplicationGroup(PanObject):
    "An application group"
    _endpoint = "/sse/config/v1/application-groups"


class ApplicationOverrideRule(PanObject):
    "An application override rule"
    _endpoint = "/sse/config/v1/app-override-rules"


class AutoTagAction(PanObject):
    "An auto-tag action"
    _endpoint = "/sse/config/v1/auto-tag-actions"


class Certificate(PanObject):
    "An X.509 certificate"
    _endpoint = "/sse/config/v1/certificates"


class CertificateProfile(PanObject):
    "A certificate profile"
    _endpoint = "/sse/config/v1/certificate-profiles"


class DynamicUserGroup(PanObject):
    "A dynamic user group"
    _endpoint = "/sse/config/v1/dynamic-user-groups"


class ExternalDynamicList(PanObject):
    "An external dynamic list"
    _endpoint = "/sse/config/v1/external-dynamic-lists"


class HipObject(PanObject):
    "A HIP object"
    _endpoint = "/sse/config/v1/hip-objects"


class HipProfile(PanObject):
    "A HIP profile"
    _endpoint = "/sse/config/v1/hip-profiles"


class Region(PanObject):
    "A region"
    _endpoint = "/sse/config/v1/regions"


class Schedule(PanObject):
    "A schedule"
    _endpoint = "/sse/config/v1/schedules"


class Service(PanObject):
    "An application group"
    _endpoint = "/sse/config/v1/services"


class ServiceGroup(PanObject):
    "A service group"
    _endpoint = "/sse/config/v1/service-groups"


class URLCategory(PanObject):
    "A custom URL category"
    _endpoint = "/sse/config/v1/url-categories"


class URLFilteringCategory(PanObject):
    "A prefined URL category"
    _endpoint = "/sse/config/v1/url-filtering-categories"
