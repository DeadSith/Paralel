from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Hi, Second Processor!", 1)
elif rank == 1:
    message = comm.recv()
    print(f'Received: {message}')