# Copy a file from windows to WSL:
# You should be able to access your Windows system under the /mnt directory.
# For example inside of bash, use this to get to your pictures directory:
# shellcheck disable=SC2217
# shellcheck disable=SC2164
cd /mnt/c/Users/<windows.username>/Pictures

# Shutdown WSL using bash
wsl.exe --shutdown
