# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    #SECRET_KEY = os.environ.get('CONDUIT_SECRET', 'secret-key')  # TODO: Change me
    SECRET_KEY="Th3k3y"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ELASTICSEARCH_HOST ='http://192.168.150.131:9200'
    ELASTICSEARCH_DATAINDEX ='asset'


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    ## config Elasticsearch
    ELASTICSEARCH_HOST ='http://192.168.150.131:9200'
    ELASTICSEARCH_DATAINDEX ='asset'

class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'
    DEBUG = True