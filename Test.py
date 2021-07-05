import win32com.client

objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect

if(bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()
