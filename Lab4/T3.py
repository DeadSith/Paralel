from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()

print(f'New group contains processes: 0 - {size - 2}')
newGroup = comm.group.Excl([size - 1])
newComm = comm.Create_group(newGroup)

if newComm != MPI.COMM_NULL:
    groupSize = newComm.Get_size()
    groupRank = newComm.Get_rank()
    if groupRank == 0:
        message = 'Hi, Parallel Programmer!'
        print(f'Sent: {message}')
        newComm.bcast(message)
    else:
        message = newComm.bcast(None)
        print(f'Received: {message}')

