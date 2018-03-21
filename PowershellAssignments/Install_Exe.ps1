$pathOfSetup=Read-Host -Prompt 'Enter the path of setup'
Start-Process -Wait -FilePath $pathOfSetup -ArgumentList "/S" 
echo "Software installed Successfully"