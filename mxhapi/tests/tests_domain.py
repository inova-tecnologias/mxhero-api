import unittest, sys, requests, json, uuid
from datetime import datetime

BASE_URL = 'http://localhost:8080'
config = {
  'domain' : {
    'get' : {
      'pass' : {
        'environment' : 'mxhdev',
        'domain' : 'abc123.com.br',
        'code' : [200]
      },
      'fail' : {
        'environment' : 'mxhdev_non_exists',
        'domain' : 'abc123.com',
        'code' : [404]
      }
    },
    'delete' : {
      'pass' : {
        'environment' : 'mxhdev',
        'domain' : 'abc123.com.br',
        #'domain' : 'abc123.com.br; UPDATE domain SET allowed_ip_masks=NULL WHERE domain = "uolhost.u.inova.com.br";', # SQL INJECTION TEST
        'code' : [200, 204],
        'body' : {}
      }
    },
    'put' : {
      'pass' : {
        'environment' : 'mxhdev',
        'domain' : 'abc123.com.br',
        'code' : [201],
        'body' : {
          'inbound_server': "mta-in.u.inova.com.br",
          'directory_type': "zimbra",
          'adsync_pass': "GPqZe2MCx",
          'adsync_port': "389",
          'adsync_host': "ldap.u.inova.com.br",
          'adsync_user': "uid=zimbra,cn=admins,cn=zimbra",
          'admin_email' : 'suporte@inova.com.br',
          'default_rules' : True
        }
      },
      'fail' : {
        'environment' : 'mxhdev',
        'domain' : 'abc123.com',
        'code' : [400, 501],
        'body' : {}
      }
    }
  }
}

HEADERS = {'Content-Type' : 'application/json'}

class DomainTestCase(unittest.TestCase):
  def get_operations(self):

    for t_type, param in config['domain']['get'].iteritems():
      url = BASE_URL + '/mxhero/%s/domain/%s' % (param['environment'], param['domain'])
      print 'testing type %s...' % t_type
      
      print 'GET:', url
      response = requests.get(url, headers=HEADERS)
      
      print response.text
      self.assertTrue(response.status_code in param['code'])



  def put_operations(self):
    for t_type, param in config['domain']['put'].iteritems():
      url = BASE_URL + '/mxhero/%s/domain/%s' % (param['environment'], param['domain'])
      print 'testing type %s...' % t_type
      
      print 'PUT:', url
      response = requests.put(url, headers=HEADERS, data=json.dumps(param['body']))
      
      print response.text
      self.assertTrue(response.status_code in param['code']) 


  def delete_operations(self):
    for t_type, param in config['domain']['delete'].iteritems():
      url = BASE_URL + '/mxhero/%s/domain/%s' % (param['environment'], param['domain'])
      print 'testing type %s...' % t_type
      
      print 'DELETE:', url
      response = requests.delete(url, headers=HEADERS)
      
      print response.status_code
      print response.text
      self.assertTrue(response.status_code in param['code'])
  

if __name__ == '__main__':
  suite = unittest.TestSuite()
  
  suite.addTest(DomainTestCase('delete_operations'))
  suite.addTest(DomainTestCase('put_operations'))
  suite.addTest(DomainTestCase('get_operations'))
  unittest.TextTestRunner().run(suite)
