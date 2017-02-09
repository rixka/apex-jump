import os
import sys
import logging
import traceback

from common import validate_request, RestfulError

class RouterCore(object):
    actions = {}

    def __call__(self, event, context=None):
        '''
          Provide an event that contains the following keys:
            - action: one of the actions in the actions dict below
            - body: a parameter to pass the payload to the action being performed
        '''

        logging.info('starting lambda_handler')
        logging.debug('event: %s', event)

        body = event.get('body', {})

        try:
            action = self.actions[event['action']]
        except KeyError:
            logging.error('action not supported: %s', event['action'])
            raise Exception('Bad Request')

        try:
            # validate_request(body, action.get('schema'))
            response = action['run'](body)
            logging.debug('response: %s', response)
            return response

        except RestfulError as e:
            logging.info('returning non 200 status code')
            logging.debug(e.message)
            raise Exception(e.message)

        except Exception as e:
            logging.critical(e)
            traceback.print_exc()
            raise Exception('Internal Error')
