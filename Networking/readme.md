- How to “ssh” into Windows WSL2 as a remote server?
  - https://medium.com/@sergioli/how-to-ssh-into-windows-wsl2-as-a-remote-server-66dc616b4f59
  - open PowerShell as administrator
  - run the following commands to download and start openssh server
    - `Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'`
    - `Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0`
    - `Set-Service -Name sshd -StartupType 'Automatic'`
    - `Start-Service sshd`
    - `Get-Service sshd`
  -  Set the WSL2 distro (suppose you only have one distro as me) to be the default shell to be accessed
    - `New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\WINDOWS\System32\bash.exe" -PropertyType String -Force`
  - Now, I successfully connect to my Windows10 WSL2 Ubuntu shell from other device (in the same LAN) via
    `ssh windows_user_name@local_ip`
    # then you need to enter your windows' login password for authentication
  - check default distro wsl2
    - `wsl --list --verbose`
  - get windows local ip
    - `(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias (Get-NetAdapter | Where-Object {$_.Status -eq "Up"}).Name -ErrorAction SilentlyContinue | Where-Object {$_.AddressFamily -eq "IPv4" -and $_.PrefixOrigin -eq "Manual"}).IPAddress`
    - `$ipAddress = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias (Get-NetAdapter | Where-Object {$_.Status -eq "Up"}).Name).IPAddress`
    - `$ipAddress`
  - `windows username`
  - `$env:USERNAME`
  - check if ssh is online for win
    - `Get-Service -Name sshd`
    - `Start-Service sshd`
  - enable firewall
    - Open Windows Defender Firewall Settings:
    - Go to the Control Panel or search for "Windows Defender Firewall" in the Start menu. 
    - Click on "Windows Defender Firewall."
    - Create an Inbound Rule:
    - Click on "Advanced settings" on the left-hand side. 
    - In the Windows Defender Firewall with Advanced Security window, click on "Inbound Rules."
    - Create a New Rule for SSH:
    - Click on "New Rule" in the right-hand pane. 
    - Select "Port" as the rule type and click "Next."
    - Choose "TCP" as the protocol and specify the port (default is 22 for SSH). Click "Next."
    - Select "Allow the connection" and click "Next."
    - Choose when the rule applies (Domain, Private, Public) and click "Next."
    - Give the rule a name (e.g., "SSH Port 22") and a description, then click "Finish."
