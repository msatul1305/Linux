ssh.md
1. SSH: Secure Shell
    - Port: 22
    - Cryptographic network protocol
    - Allows secure remote login and command execution over unsecured network.
    - Provides secure and encrypted channel for communication between 2 devices: client and server.
    - Operating Model:
        - Client-Server Connection
        - Encryption and Authentication
        - User Authentication
        - Session creation
    - Uses of SSH:
        - Remote Login
        - Secure File Transfer: over SCP(Secure Copy) or SFTP(SSH File Transfer Protocol)
        - Tunneling:
            - encapsulating one network protocol within another creating tunnel allowing encapsulated data to be transmitted securely and privately over untrusted network.
            - Outer protocol used for transmitting encapsulated data across the network
            - Inner protocol used for encapsulating original data being transmitted(e.g. SSH or VPN)
            - allow users to securely route network connections using SSH
            - also used to bypass network restrictions, overcome network topology limitations.
                - e.g. if some port/protocol is blocked, we can tunnel restricted traffic via different protocol which is allowed.
            - e.g. of tunneling protocols
                - SSH
                - VPN protocols like IP secs(Internet Protocol Security), OpenVPN
                - GRE(Generic Routing Encapsulation): point-2-point tunneling between 2 endpoints. Used for connecting VPN or remote networks.
                - Layer2 Tunneling(l2TP):
                    - PPTP(Point to P Tunneling Protocol)+ L2F(Layer 2 Forwarding).
                    - Used to secure tunnels for remote access.
        - Remote command executions
    - used in Windows, Linux. macOS all.
    - Created using local port forwarding, remote port forwarding, dynamic port forwarding
2. RDP: Remote Desktop Protocol
    - Port: 3389
    - By Microsoft
    - for remote desktop control
  