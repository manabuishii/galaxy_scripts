#!/usr/bin/env python
import os
import bioblend
from bioblend import galaxy
docker_bioblend_galaxy_host=os.environ['DOCKER_BIOBLEND_GALAXY_HOST']
docker_bioblend_galaxy_api_key=os.environ['DOCKER_BIOBLEND_GALAXY_API_KEY']
if docker_bioblend_galaxy_host and docker_bioblend_galaxy_api_key:
  global gi
  gi = galaxy.GalaxyInstance(url=docker_bioblend_galaxy_host, key=docker_bioblend_galaxy_api_key)
