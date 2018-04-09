Get-Process | Sort CPU -Descending | select -First 1 ProcessName,Cpu >'Task_Manager.text'
Get-WmiObject win32_processor | select LoadPercentage  >>'a.text'
