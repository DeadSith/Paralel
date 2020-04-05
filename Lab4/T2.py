from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    numbers = input().split()
    print(f'Sent: {numbers}')
    comm.bcast(numbers)
else:
    numbers = comm.bcast(None)
    message = ','.join(numbers)
    print(f'Received: {message}')
