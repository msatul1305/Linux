# Linux Account Files – Compare & Contrast (Ubuntu/RHEL)

Here’s a clean **compare & contrast table** of the main Linux account-related files (Ubuntu/RHEL applicable).

---

## 🔐 Core Authentication & Account Files

| File                   | Purpose                                             | Stores Password?                  | Who Can Read | Who Can Modify | Used During Login?                  | Used During User Creation? |
|------------------------|-----------------------------------------------------|-----------------------------------|--------------|----------------|-------------------------------------|----------------------------|
| `/etc/passwd`          | User account metadata                               | ❌ No (only `x` placeholder)       | Everyone     | root           | ✅ Yes (username lookup, UID, shell) | ✅ Yes (entry created)      |
| `/etc/shadow`          | Encrypted password hashes + aging info              | ✅ Yes                             | root only    | root           | ✅ Yes (password verification)       | ✅ Yes (entry created)      |
| `/etc/login.defs`      | Default account creation & password policy settings | ❌ No                              | Everyone     | root           | ❌ No (indirect only)                | ✅ Yes (read by `useradd`)  |
| `/etc/default/useradd` | Default values for `useradd`                        | ❌ No                              | Everyone     | root           | ❌ No                                | ✅ Yes                      |
| `/etc/group`           | Group definitions                                   | ❌ No (group password rarely used) | Everyone     | root           | ✅ Yes (group membership)            | ✅ Yes                      |
| `/etc/gshadow`         | Secure group password file                          | ✅ Yes (group password)            | root only    | root           | ⚠️ Rarely                           | ✅ Yes                      |
| `/etc/pam.d/*`         | Authentication policy control                       | ❌ No (controls behavior)          | Everyone     | root           | ✅ YES (very important)              | ⚠️ Indirect                |

---

## 🧠 Field-Level Comparison

| Aspect               | `/etc/passwd`                    | `/etc/shadow`                    | `/etc/login.defs`     |
|----------------------|----------------------------------|----------------------------------|-----------------------|
| Format               | Colon-separated                  | Colon-separated                  | Key-value pairs       |
| Example Entry        | `atul:x:1000:1000:...:/bin/bash` | `atul:$y$...:19700:0:99999:7:::` | `PASS_MAX_DAYS 99999` |
| Password Location    | Placeholder only                 | Actual hash                      | Not stored            |
| Password Expiry Info | ❌ No                             | ✅ Yes                            | Default values only   |
| Security Sensitivity | Medium                           | High                             | Low                   |

---

## 🔑 Password-Related Comparison

| Feature                   | `/etc/passwd` | `/etc/shadow`  | PAM (`/etc/pam.d/`) |
|---------------------------|---------------|----------------|---------------------|
| Password hash stored      | ❌             | ✅              | ❌                   |
| Password expiry days      | ❌             | ✅              | May enforce         |
| Password complexity       | ❌             | ❌              | ✅                   |
| Account locking           | ❌             | ✅ (`!` or `*`) | ✅                   |
| Hashing algorithm control | ❌             | ❌              | ✅                   |

---

## 🐧 Ubuntu vs RHEL Behavior (Important Difference)

| Feature                | Ubuntu                | RHEL/CentOS        |
|------------------------|-----------------------|--------------------|
| Default hash algorithm | yescrypt (`$y$`)      | SHA-512 (`$6$`)    |
| Main policy control    | PAM dominant          | `login.defs` + PAM |
| SELinux                | ❌ Disabled by default | ✅ Enabled          |
| AppArmor               | ✅ Yes                 | ❌ No (default)     |

---

## 🔄 When Each File Is Used

| Operation                   | Files Involved                                                                        |
|-----------------------------|---------------------------------------------------------------------------------------|
| Create user (`useradd`)     | `/etc/login.defs`, `/etc/default/useradd`, `/etc/passwd`, `/etc/shadow`, `/etc/group` |
| Change password (`passwd`)  | `/etc/shadow`, PAM                                                                    |
| Login attempt               | `/etc/passwd`, `/etc/shadow`, PAM                                                     |
| Check group membership      | `/etc/group`                                                                          |
| Enforce password complexity | PAM only                                                                              |

---

## 🏗 Simple Mental Model

| Category    | Files                            |
|-------------|----------------------------------|
| 📁 Identity | `/etc/passwd`                    |
| 🔐 Secrets  | `/etc/shadow`, `/etc/gshadow`    |
| 📜 Policy   | `/etc/login.defs`, `/etc/pam.d/` |
| 👥 Groups   | `/etc/group`                     |

- prevent a user from logging in
  - in shadow file, add `!` or `*` before the password hash to lock the account
  - in passwd file, change the shell to `/sbin/nologin` or `/bin/false` to prevent login
  - in login.defs, set `PASS_MAX_DAYS` to 0 to expire the password immediately, but this is less common for locking accounts
- syntax in passwd file: `atul:x:1000:1000:...:/bin/bash`
  - Meaning of each field:
    - `atul`: username
    - `x`: password placeholder (actual hash is in shadow file)
    - `1000`: user ID (UID)
      - 1000 is the first non-system user ID on most Linux distributions, 
      - so this indicates a regular user account
    - `1000`: group ID (GID)
      - 1000 is the primary group for this user, which usually has the same name as the username
    - `...`: user info (e.g., full name, contact info)
    - `/bin/bash`: default shell
  - Allowed changes to lock account:
    - change shell to `/sbin/nologin` or `/bin/false`
    - change password field to `!` or `*` to prevent password authentication
- syntax in shadow file: `atul:$y$...:19700:0:99999:7:::`
  - Meaning of each field:
    - `atul`: username (must match passwd file)
    - `$y$...`: password hash (using yescrypt in Ubuntu)
    - `19700`: last password change date (days since Jan 1, 1970)
    - `0`: minimum password age (days before change allowed)
    - `99999`: maximum password age (days before expiration)
    - `7`: warning period (days before expiration to warn user)
    - `:::`: reserved fields for inactivity and account expiration, usually left empty
  - Allowing changes to lock account:
    - change password hash to `!` or `*` to prevent password authentication
- complete syntax of login.defs file:
  - `PASS_MAX_DAYS 99999`: maximum password age (days before expiration)
  - `PASS_MIN_DAYS 0`: minimum password age (days before change allowed)
  - `PASS_WARN_AGE 7`: warning period (days before expiration to warn user)
  - `UID_MIN 1000`: minimum user ID for regular users
  - `GID_MIN 1000`: minimum group ID for regular groups
  - `UMASK 022`: default file permissions for new files (e.g., 755 for directories, 644 for files)
- command to update the password for a user:
  - `passwd atul` (will prompt for new password and update shadow file)