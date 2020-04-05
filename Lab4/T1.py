from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    message = 'Hi, Parallel Programmer!'
    print(f'Sent: {message}')
    comm.bcast(message)
else:
    message = comm.bcast(None)
    print(f'Received: {message}')
