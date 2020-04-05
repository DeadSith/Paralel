from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
res = None
if rank == 0:
    a = [10, 11, 8, 9, 5, 9, 7, 12, 11, 5, 4, 2 ]
    for i in range(1, size):
        data = a[(i-1)*4:i*4]
        print(f'Sending data {data} to worker {i}.')
        comm.send(data, i)
    res = comm.reduce(math.inf, op=MPI.MIN)
else:
    message = comm.recv()
    print(f'Rank {rank} received: {message}')
    prod = math.prod(message)
    print(f'Sending product: {prod} from rank {rank}.')
    res = comm.reduce(prod, op=MPI.MIN)

print(f'Recieved result: {res} in rank {rank}.')