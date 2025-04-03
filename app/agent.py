import json
import os

from initiator_agent import initiator_agent, initiator_protocol, bureau
from response_agent import bruno_agent, bruno_protocol

if __name__ == '__main__':
    bureau.run()