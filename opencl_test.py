import pyopencl as cl

print(cl.get_platforms())

for platform in cl.get_platforms():
    print(platform.get_devices())