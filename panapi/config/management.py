#!/usr/bin/env python3

from panapi.config import PanObject

class Job(PanObject):
    'A management job'
    _endpoint = '/sse/config/v1/jobs'
    
    def poll(self):
        #TODO: Add synchronous job poller
        pass


class ConfigVersion(PanObject):
    'A config version'
    _endpoint = '/sse/config/v1/config-versions'
    
    def push(self):
        #TODO: Add push for candidate or version 
        pass
    
    
    def load(self):
        #TODO: Add version loader
        pass