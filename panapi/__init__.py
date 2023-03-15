#!/usr/bin/env python3

# import json
import yaml
import os
import jwt
from jwt import PyJWKClient
from jwt.exceptions import ExpiredSignatureError
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class PanApiSession(OAuth2Session):
    """PanApi extension to :class:`requests_oauthlib.OAuth2Session`.

    Methods
    -------
    authenticate(self, **kwargs)
        Create the OAuth2 session and request an access token

    validate(self)
        Validate the OAuth2 session's access token

    refresh(self)
        Request a new OAuth2 access token for the session

    decode_token(self)
        Validate the JWT token contents and signature

    Properties
    ----------
    is_expired
        Has the the access token expired?
    """

    _configfile = "~/.panapi/config.yml"

    def authenticate(self, token_url = 'https://auth.apps.paloaltonetworks.com/am/oauth2/access_token', **kwargs):
        self.token_url = 'https://auth.apps.paloaltonetworks.com/am/oauth2/access_token'
        # Process the configfile or kwargs
        keys = ("client_id", "client_secret", "tsg_id")
        if set(keys).issubset(kwargs):
            self.client_id = kwargs.get("client_id")
            self.client_secret = kwargs.get("client_secret")
            self.tsg_id = kwargs.get("tsg_id")
        else:
            if "configfile" in kwargs:
                self._configfile = kwargs.get("configfile")
            f = os.path.abspath(
                os.path.expanduser(os.path.expandvars(self._configfile))
            )
            with open(f, "r", encoding="utf-8-sig") as c:
                config = yaml.safe_load(c.read())
            self.client_id = config["client_id"]
            self.client_secret = config["client_secret"]
            self.tsg_id = config["tsg_id"]
        # Fix the scope to include email and profile
        self.scope = "email profile tsg_id:" + str(self.tsg_id)
        # Request the access token and retrieve the issuer's signing key
        oauth2_client = BackendApplicationClient(
            client_id=self.client_id, scope=self.scope
        )
        self._client = oauth2_client
        self.fetch_token(
            token_url=self.token_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        # Retrieve the signing key for token validation
        jwks_uri = (
            "/".join(self.token_url.split("/")[:-1]) + "/connect/jwk_uri"
        )
        jwks_client = PyJWKClient(jwks_uri)
        self.signing_key = jwks_client.get_signing_key_from_jwt(
            self.access_token
        )

    def reauthenticate(self):
        self.fetch_token(
            token_url=self.token_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )

    def decode_token(self):
        payload = jwt.decode(
            self.access_token,
            self.signing_key.key,
            algorithms=["RS256"],
            audience=self.client_id,
            options={"verify_exp": False, "verify_iat": False},
        )
        return payload

    @property
    def is_expired(self):
        try:
            jwt.decode(
                self.access_token,
                self.signing_key.key,
                algorithms=["RS256"],
                audience=self.client_id,
            )
        except ExpiredSignatureError:
            return True
        else:
            return False
