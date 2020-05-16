# Algorithm 5.2.2M Knuth "Sorting and Searching" (page 111 or 122 in PDF)
from mpi4py import MPI
import math

data = [10, 11, 8, 9, 5, 9, 7, 12, 11, 5, 4, 2]
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
n = len(data)
t = math.ceil(math.log2(n))

# original loop for finding all pairs
#if (rank == 0):
#    pairs = []
#    p = 2 ** (t - 1)
#    while p > 0:
#        q = 2 ** (t - 1)
#        r = 0
#        d = p
#        while d > 0:
#            for i in range(0, n - d):
#                if i & p == r:
#                    pairs.append([i, i + d])
#            d = q - p
#            q //= 2
#            r = p
#        p //= 2
#    print(pairs)

cur_element = data[rank]

pairs = []
p = 2 ** (t - 1)
i = rank
while p > 0:
    q = 2 ** (t - 1)
    r = 0
    d = p
    while d > 0:
        i = rank - d
        if i >= 0 and i < (n - d) and i & p == r:
            pairs.append([i, i + d])
        else:
            i = rank
            if i < (n - d) and i & p == r:
                pairs.append([i, i + d])
        d = q - p
        q //= 2
        r = p
    p //= 2

def compare(dest, our, their):
    if rank < dest:
        return min([our, their])
    else:
        return max([our, their])

for pair in pairs:
    dest = pair[0]
    if dest == rank:
        dest = pair[1]
    #comm.send(cur_element, dest=dest)
    #their = comm.recv(source=dest)
    their = comm.sendrecv(cur_element, dest=dest, source=dest)
    cur_element = compare(dest, cur_element, their)

sorted_arr = comm.gather(cur_element, root=0)

if rank == 0:
    print(f'Sorted array: {sorted_arr}')
