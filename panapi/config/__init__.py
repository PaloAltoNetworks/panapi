#!/usr/bin/env python3


class PanObject:
    """Base class for all resource objects

    This class defines a configuration object that can defined in Palo Alto Networks Unified Cloud Manager. 
    """
    _base_url = 'https://api.sase.paloaltonetworks.com'
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
  

    def __str__(self):
        return str(self.__dict__)  
    

    def create(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint
        headers = {'Content-Type': 'application/json'}
        params = {'folder': self.folder}
        try:
            session.response = session.post(
                url = url,
                headers = headers,
                params = params,
                json = self.payload
            )
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 201:
                config = session.response.json()
                self.id = config.get('id')


    def read(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint
        params = {'folder': self.folder}
        has_id = hasattr(self, 'id')
        has_name = hasattr(self, 'name')
        if has_id:
            url = self._base_url + self._endpoint + '/{}'.format(self.id)
        elif has_name:
            params.update({'name': self.name})
        else:
            raise ValueError('name or id value is required')
        try:
            session.response = session.get(
                url = url,
                params = params
            )
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 200:
                result = session.response.json()
                if has_id:
                    return type(self)(**result)
                elif has_name:
                    config = result['data'][0]
                    return type(self)(**config)


    def list(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint
        params = {'folder': self.folder}
        try:
            session.response = session.get(
                url = url,
                params = params
            )
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 200:
                result = session.response.json()
                obj_list = []
                for config in result['data']:
                    obj_list.append(type(self)(**config))
                return obj_list

                
    def update(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + '/{}'.format(self.id)
        headers = {'Content-Type': 'application/json'}
        params = {'folder': self.folder}
        try:
            session.response = session.put(
                url = url,
                headers = headers,
                params = params,
                json = self.payload
            )
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 200:
                config = session.response.json()
            # return config


    def delete(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + '/{}'.format(self.id)
        headers = {'Content-Type': 'application/json'}
        params = {'folder': self.folder}
        try:
            session.response = session.delete(
                url = url,
                headers = headers,
                params = params
            )
        except Exception as err:
            print(err)
        else:
            if session.response.status_code == 200:
                del(self)


    @property
    def payload(self):
        items = {k:v for k,v in self.__dict__.items() if k not in {'folder', 'id'}}
        return items