from marshmallow import Schema, fields

class DomainSchema(Schema):
  domain = fields.String(required=True) 
  creation = fields.DateTime()
  server = fields.String(required=True)
  updated = fields.DateTime()
  cos = fields.String()
  allowed_ip_masks = fields.String()
  allowed_transport_agents = fields.String()
  address = fields.String(required=True)
  base = fields.String(required=True)
  directory_type = fields.String(required=True)
  next_update = fields.DateTime(required=True)
  override_flag = fields.String(required=True)
  user = fields.String(required=True)
  port = fields.String(required=True)
  total_users = fields.Integer()

class MxheroSchema(Schema):
  name = fields.String(required=True)
  db_host = fields.String(required=True)
  #db_name = fields.String(required=True)
  #db_user = fields.String(required=True)
  #db_pass = fields.String(required=True)
  #db_port = fields.Integer(required=True)
