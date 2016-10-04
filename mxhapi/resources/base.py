from flask.ext.restful import reqparse, request, Resource, abort
from mxhapi.components.common import logger, cfg
from mxhapi.components.domain import Domain


def abort_if_object_doesnt_exist(mxhero, scope):

  if mxhero in cfg['environment']:
    if scope == 'domain':
      try:
        d = Domain(mxhero)
        return d
      except Exception, e:
        err_message = 'error retrieving domain object'
        logger.error('%s: %s' % (err_message, e))
        abort(501, message=err_message)
    elif scope == 'mxhero':
      return
    else:
      err_message = 'scope not supported %s' % scope
      logger.error('%s: %s' % (err_message, e))
      abort(501, message=err_message)
  else:
    err_message = 'mxHero instalation does not exists %s' % mxhero 
    abort(404, message=err_message)

class BaseResource(Resource):
  def __init__(self, **kwargs):
    parser = reqparse.RequestParser(bundle_errors=True)
    self.parser = reqparse.RequestParser()