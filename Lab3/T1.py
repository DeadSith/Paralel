from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    comm.send('0', 1)
    message = comm.recv()
    print(f'Received: {message}')
elif rank != size - 1:
    message = comm.recv() + f',{rank}'
    comm.send(message, rank + 1)
else:
    message = comm.recv() + f',{rank}'
    comm.send(message, 0)