# encoding: utf-8
        
class DebugBackend:
    """Debug backend that prints SMS to console."""
    
    class SMS:
    
        @classmethod
        def send(self, recipient, sender, price, country, message):

            text  = 'SMS ----------------------------\n'
            text += 'Recipient: %s\n' % recipient
            text += 'Sender: %s\n' % sender
            text += 'Country: %s\n' % country
            text += 'Price: %s\n' % price
            text += 'Message: %s\n' % message
            text += '---------------------------------\n'

            print text

            return 1
            
        @classmethod
        def receive(self):
            raise NotImplementedError()