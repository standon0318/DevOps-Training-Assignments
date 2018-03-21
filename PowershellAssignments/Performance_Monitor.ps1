
echo ($DiskSpace = Get-Counter -counter "\LogicalDisk(_Total)\% Free Space").CounterSamples.CookedValue
echo $CPUTime=(Get-Counter -counter "\Processor(_Total)\% Processor Time”).CounterSamples.CookedValue

echo $AvailableMBytes=(Get-Counter -counter "\Memory\Available MBytes”).CounterSamples.CookedValue
echo "Processor Performance="(Get-Counter -counter '\TCPv6\Connections Active').CounterSamples.CookedValue
echo "File Write Operations="(Get-Counter -counter '\System\File Write Operations/sec').CounterSamples.CookedValue