import json
from flask.ext.restful import reqparse, request, Resource, abort
from mxhapi.resources.base import BaseResource, abort_if_object_doesnt_exist
from mxhapi.models.schemas import MxheroSchema
from mxhapi.components.common import logger, cfg


class DomainResource(BaseResource):
  def __init__(self):
    super(DomainResource, self).__init__()

  def get(self, mxhero, domain_name):
    d = abort_if_object_doesnt_exist(mxhero, scope='domain')

    try: 
      return d.get(domain_name)
    except Exception, e:
      abort(404,message='could not get domain %s' % domain_name)


  def put(self, mxhero, domain_name):
    d = abort_if_object_doesnt_exist(mxhero, scope='domain')

    self.parser.add_argument('inbound_server', type=str, required=True)
    self.parser.add_argument('adsync_host', type=str, required=True)
    self.parser.add_argument('adsync_port', type=str, required=True)
    self.parser.add_argument('adsync_user', type=str, required=True)
    self.parser.add_argument('adsync_pass', type=str, required=True)
    self.parser.add_argument('directory_type', type=str, required=True)
    self.parser.add_argument('admin_email', type=str, required=True)
    self.parser.add_argument('default_rules', type=bool)
    reqdata = self.parser.parse_args()

    return d.create(domain_name, reqdata)

  def delete(self, mxhero, domain_name):
    d = abort_if_object_doesnt_exist(mxhero, scope='domain')

    return d.delete(domain_name)
