import numpy as np
from mpi4py import MPI
import time

data_size = 1000 * 1000
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

cur_data = None
cur_size = data_size // size

start_time = None

if rank == 0:
    data = np.random.randint(0, data_size, size=data_size)
    start_time = time.process_time_ns()
    for i in range(1, size):
        cur_data = data[i*cur_size:(i+1)*cur_size]
        comm.send(cur_data, i)
    cur_data = data[0:cur_size]
else:
    cur_data = comm.recv(source=0)

cur_max = np.max(cur_data)
res = comm.reduce(cur_max, op=MPI.MAX)

if rank == 0:
    end_time = time.process_time_ns()
    print(f'Time spent on computing: {end_time - start_time} nanoseconds.')
    print(f'Recieved result: {res} in rank {rank}.')

