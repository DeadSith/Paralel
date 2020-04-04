from mpi4py import MPI
import sys

arg_len = len(sys.argv)
if arg_len != 3:
    print(f'Expected 2 arguments, got {arg_len - 1}')
    exit()

sender = int(sys.argv[1])
reciever = int(sys.argv[2])

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == sender:
    message = f'Sending from {rank}'
    comm.send(message, 0)
elif rank == reciever:
    message = comm.recv(source=0)
    message += f'Recieved in {rank}'
    print(message)
elif rank == 0:
    message = comm.recv(source=sender)
    message = f'{message}\nPassing through 0\n'
    comm.send(message, reciever)

