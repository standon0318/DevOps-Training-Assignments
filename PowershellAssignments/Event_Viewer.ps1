$getLogsForTime=Read-Host -Prompt "Enter the time period for logs"
$getLogsForType=Read-Host -Prompt "Enter the type of logs required"
$getLogsTime=(Get-Date).AddHours(-$getLogsForTime)
Get-EventLog -LogName $getLogsForType -EntryType Information -After $getLogsTime| Export-Csv -Path "process.csv" 