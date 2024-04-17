Installation:
PowerShell 7.3.5 (universal package) for any supported version of Ubuntu
https://github.com/PowerShell/PowerShell/releases/download/v7.3.5/powershell_7.3.5-1.deb_amd64.deb
# Install the downloaded package
sudo dpkg -i powershell-lts_7.3.5-1.deb_amd64.deb

# Resolve missing dependencies and finish the install (if necessary)
sudo apt-get install -f

# Run powershell
pwsh

# TEST
Invoke-WebRequest https://google.com
