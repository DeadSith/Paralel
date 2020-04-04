from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank != size - 1:
    comm.send(rank, rank + 1)
else:
    comm.send(rank, 0)

message = comm.recv()
print(message)
