from multiprocessing import shared_memory, Process


a = [1, 2, 3]
shm = shared_memory.SharedMemory(create=True, size=len(a), name='2')
shm.buf[:len(a)] = bytearray(a)

exist_shm = shared_memory.SharedMemory(name='2')
print(exist_shm.buf.tolist()[:len(a)])
