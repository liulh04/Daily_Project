#原神，启动！
import requests
url = u="https://v2.kwaicdn.com/ksc2/KhJrtZfqNTnEvneKpXAlY5wh7MU5MG4C14T7YK-9eICYAwSMvHwYkiCzQ6wl_Sjc8k7NNN2qrwAHgdBLNgXyicGNcp1Z_YB1MwGdpF54v0A0ASVY0z1ecTsljgEMTKDoqJgyQOBS6ic8eZ3Hzq8jgu6UpgTCC8wLSFUmOIqFxQ4xwwJuvHjRCbNYotaiQBld.mp4?pkey=AAV7gsX64jOFQm1k4ssrrRBIYos3esmkLeqL2m3_cEL7qa8jsui6-_1W2np7EOS8dTuBh9zk1aKdv772hjyuGJ6tGzwJ2pewVtB03iXEZgSFrleLqjnliLLPUHmb7kS9g60&tag=1-1697809514-unknown-0-5wcacylfq3-4f612202031783ec&clientCacheKey=3xvy8k679seafp6_b.mp4&di=718c034b&bp=10004&tt=b&ss=vp"
res = requests.get(url)
open('原神，启动！.mp4', 'wb').write(res.content)


