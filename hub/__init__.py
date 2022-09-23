import deeplake

for k in dir(deeplake):
    exec(f"{k}=deeplake.{k}")
