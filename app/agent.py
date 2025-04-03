import json
import os

#from response_agent import bruno_agent, bruno_protocol
#from initiator_agent import initiator_agent, initiator_protocol, bureau
from testing_deltav_1 import agentDeltaV

if __name__ == '__main__':
#   uncomment this to run your agent to get prices from cmc
#    bruno_agent.run()
#   uncomment this to test communication between two agents and test behaviour
#    bureau.run()
#   uncommet this to test DeltaV
    agentDeltaV.run()