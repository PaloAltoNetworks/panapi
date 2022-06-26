#!/usr/bin/env python3

from panapi.base import PanObject

class AddressObject(PanObject):
    'An address object'
    _endpoint = '/sse/config/v1/addresses'
    

class AddressGroups(PanObject):
    'An address group'
    _endpoint = '/sse/config/v1/address-groups'
    

class Applications(PanObject):
    'An application object'
    _endpoint = '/sse/config/v1/applications'
    
    
class ApplicationFilters(PanObject):
    'An application filter'
    _endpoint = '/sse/config/v1/application-filters'
    
    
class ApplicationGroups(PanObject):
    'An application group'
    _endpoint = '/sse/config/v1/application-groups'


class AutoTagActions(PanObject):
    'An auto-tag action'
    _endpoint = '/sse/config/v1/auto-tag-actions'
    
    
class Certificates(PanObject):
    'An X.509 certificate'
    _endpoint = '/sse/config/v1/certificates'
    

class CertificateProfiles(PanObject):
    'A certificate profile'
    _endpoint = '/sse/config/v1/certificate-profiles'
    

class DynamicUserGroups(PanObject):
    'A dynamic user group'
    _endpoint = '/sse/config/v1/dynamic-user-groups'
    

class ExternalDynamicLists(PanObject):
    'An external dynamic list'
    _endpoint = '/sse/config/v1/external-dynamic-lists'
    

class HipObjects(PanObject):
    'A HIP object'
    _endpoint = '/sse/config/v1/hip-objects'
    
    
class HipProfiles(PanObject):
    'A HIP profile'
    _endpoint = '/sse/config/v1/hip-profiles'
    
    
