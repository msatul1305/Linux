- view GUI appplictions in wsl
  - Install X server on your Windows machine and 
  - set up the DISPLAY environment variable in WSL to point to the X server. 
  - Here's a general outline of the steps:
    - Install an X server on Windows:
      - You can use X410, VcXsrv, or any other X server for Windows.
      - Install the X server and start it. 
    - Set the DISPLAY environment variable in WSL:
      - Open a terminal in WSL and set the DISPLAY variable to point to your Windows machine's IP address and the display number used by the X server. 
      - Replace IP_ADDRESS with your Windows machine's IP address:
      - export DISPLAY=IP_ADDRESS:0 
      - If you are using X410, the IP address should be localhost.