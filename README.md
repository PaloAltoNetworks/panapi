# panapi

This is a lightweight Python SDK designed to interact with Palo Alto Networks Cloud Management API. It consists of an object-oriented library that simplifies OAuth 2.0 session estalishment, access token validation, and automatic access token refresh. Each configuration API endpoint is represented as unique object instances that provide a common set of create, read, update, delete, and list functions.

---

## Features

- OAuth 2.0 session management (subclassed from requests_oauthlib.Session)
- Supports credential config file (~/panapi/config)
- JSON Web Key Set (JWKS) retrieval
- JWT access token decoding and validation
- Common create, read, update, delete, and list methods for all config objects
- Automatic and transparent access token refresh

---

## Installation

Upgrade to the latest pip

```bash
pip install --upgrade pip
```

Install using pip

```bash
pip install panapi
```

Upgrade to the latest version

```bash
pip install --upgrade panapi
```

---

## Configuration

The Cloud Management API utilizes OAuth 2.0 to authenticate and authorize incoming API calls. This requires requesting an access token from an Authorization Server. The credentials needed to request an access token can be defined in a configuration located at `$HOME/.panapi/config.yml`.

```yml
---
#
# my-tenant
#
client_id: apitest@1808050139.iam.panserviceaccount.com
client_secret: feea5864-f557-11ec-b939-0242ac120002
scope: tsg_id:1808050139
token_url: https://auth.apps.paloaltonetworks.com/am/oauth2/access_token
```

---

## Usage

The following is a brief overview of how to use the `pan-api-python` SDK. For comprehensive details on its usage, please refer to the documentation [here](https://www.lipsum.com).

### Import the modules

The entire SDK can be imported into your project.

```py
import panapi
```

Specific modules can be imported as well.

```py
from panapi.config import security, network
```

Individual classes can also be imported.

```py
from panapi.config.network import RemoteNetwork, IKEGateway, IPSecTunnel
```

### Establish the OAuth 2.0 session

Instantiate the `PanApiSession` handler and authenticate to the Authorization Server.

```py
session = panapi.PanApiSession()
session.authenticate()
```

If successful, the access token will become an attribute of the `PanApiSession` instance.

```py
session.access_token
```

Token validation is done automatically with each API call using the `pan-api-python` SDK. However, manual validation of the JWT token claims and cryptographic signature can be done as well.

```py
session.is_valid
```

### Working with configuration objects

Instantiate a new configuration object.

```py
addr1 = panapi.config.objects.Address(
    folder = 'Shared',
    name = 'server1',
    ip_netmask = '10.0.100.150',
    description = 'App server 1',
    tags = ['production']
    )
```

Create the new configuration on the cloud management tenant.

```py
addr1.create(session)
```

The HTTP status code resulting from `PanApiSession` API transactions attached to the session instance.

```py
result = session.status_code
```

Retrieve a configuration object by name.

```py
gw1 = panapi.config.network.IKEGateway(
    folder = 'Remote Networks',
    name = 'Seattle-GW'
    )
```

Display the JSON payload of a configuration object.

```py
json.dumps(gw1.payload, indent=4)
```

Update elements of a configuration object.

```py
rule = panapi.config.security.SecurityRule(
    folder = 'Shared',
    named = 'Allow monitoring'
    )
rule1.read(session)
rule1.applications = ['snmpv2', 'snmpv3']
rule1.description = 'Allow SNMPv2 and v3 from NOC'
rule1.update(session)
```

Delete a configuration from the cloud management tenant.

```py
id1 = panapi.config.identity.SAMLProfile(
    folder = 'Shared',
    name = 'AD-SAML'
    )
id1.read(session)
id1.delete(session)
```
