from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank % 2 == 0:
    if rank + 1 != size:
        comm.send(rank, rank + 1)
else:
    if rank != 0:
        message = comm.recv()
        print(f'Received: {message}')