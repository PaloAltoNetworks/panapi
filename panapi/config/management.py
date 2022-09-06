#!/usr/bin/env python3

from panapi.config import PanObject

class Job(PanObject):
    'A management job'
    _endpoint = '/sse/config/v1/jobs'
    
    def poll(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + '/' + str(self.id)
        headers = {'Content-Type': 'application/json'}
        try:
            session.response = session.get(
                url = url,
                headers = headers,
            )
        except Exception as err:
            print(err)
        else:   
            if session.response.status_code == 200:
                result = self(session.response.json()['data'][0])
                return result


class ConfigVersion(PanObject):
    'A config version'
    _endpoint = '/sse/config/v1/config-versions'
    
    def push(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + '/candidate:push'
        headers = {'Content-Type': 'application/json'}
        try:
            session.response = session.post(
                url = url,
                headers = headers,
                json = self.payload
            )
        except Exception as err:
            print(err)
        else:
            job_id = session.response.json().get('job_id')
            return Job(job_id=job_id)


    def load(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + '/{}:load'.format(self.version)
        headers = {'Content-Type': 'application/json'}
        try:
            session.response = session.post(
                url = url,
                headers = headers,
                json = self.payload
            )
        except Exception as err:
            print(err)
