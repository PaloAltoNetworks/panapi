#!/usr/bin/env python3

# from platform import version
from panapi.config import PanObject


class Job(PanObject):
    "A management job"
    _endpoint = "/sse/config/v1/jobs"


class ConfigVersion(PanObject):
    "A config version"
    _endpoint = "/sse/config/v1/config-versions"

    def push(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + "/candidate:push"
        headers = {"Content-Type": "application/json"}
        try:
            session.response = session.post(url=url, headers=headers, json=self.payload)
        except Exception as err:
            print(err)
        else:
            job_id = session.response.json().get("job_id")
            return Job(id=job_id)

    def load(self, session):
        if session.is_expired:
            session.reauthenticate()
        url = self._base_url + self._endpoint + ":load"
        headers = {"Content-Type": "application/json"}
        # TODO Fix this once the endpoint supports POST by ID
        # body = {"version": self.id}
        try:
            session.response = session.post(
                url=url,
                headers=headers,
                # TODO Change back to self.payload once the endpoint supports POST by ID
                json=self.body,
            )
        except Exception as err:
            print(err)
