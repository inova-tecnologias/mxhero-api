import json
from flask.ext.restful import reqparse, request, Resource, abort
from mxhapi.resources.base import BaseResource, abort_if_object_doesnt_exist
from mxhapi.models.schemas import MxheroSchema
from mxhapi.components.common import logger, cfg

class MxheroResource(BaseResource):
  def __init__(self):
    super(MxheroResource, self).__init__()

  def get(self, mxhero):
    abort_if_object_doesnt_exist(mxhero, scope='mxhero')

    res = MxheroSchema(many=False).dump(cfg['environment'][mxhero])
    return {
      'message' : res.data
    }, 200