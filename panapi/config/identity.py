#!/usr/bin/env python3

from panapi.config import PanObject

class AuthenticationPortal(PanObject):
    'An authentication portal'
    _endpoint = '/sse/config/v1/authentication-portals'


class AuthenticationProfile(PanObject):
    'An authentication profile'
    _endpoint = '/sse/config/v1/authentication-profiles'
    
    
class AuthenticationRule(PanObject):
    'An authentication rule'
    _endpoint = '/sse/config/v1/authentication-rules'
    
    
class AuthenticationSequence(PanObject):
    'An authentication sequence'
    _endpoint = '/sse/config/v1/authentication-sequences'
    
    
class KerberosServiceProfile(PanObject):
    'A Kerberos server profile'
    _endpoint = '/sse/config/v1/kerberos-server-profiles'
    
    
class LDAPServerProfile(PanObject):
    'An LDAP server profile'
    _endpoint = '/sse/config/v1/ldap-server-profiles'
    
    
class LocalUser(PanObject):
    'A local user'
    _endpoint = '/sse/config/v1/local-users'
    
    
class MFAServer(PanObject):
    'A multi-factor authentication server'
    _endpoint = '/sse/config/v1/mfs-servers'
    
    
class RADIUSServerProfile(PanObject):
    'A RADIUS server profile'
    _endpoint = '/sse/config/v1/radius-server-profiles'
    
    
class SAMLServerProfile(PanObject):
    'A SAML server profile'
    _endpoint = '/sse/config/v1/saml-server-profiles'
    
    
class TACACSServerProfile(PanObject):
    'A TACACS server profile'
    _endpoint = '/sse/config/v1/tacacs-server-profiles'