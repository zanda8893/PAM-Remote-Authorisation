# PAM Remote Authorisation


## Installation

Ensure you have the required dependencies installed before proceeding e.g. gcc python3.11

```console
// clone the repo
$ git clone https://github.com/zanda8893/PAM-Remote-Authorisation

// change the working directory to PAM-Remote
$ cd PAM-Remote-Authorisation

// Build the PAM
$ make

// Install (root required)
# make install
```

## Usage
Place your discord token in the config
```
/etc/remote_auth.conf:

# Discord
DISCORD_TOKEN=[Token Here]
```
Enable the PAM (sudo)

`/etc/pam.d/sudo:`
```
#%PAM-1.0
auth sufficient /usr/lib/security/pam_remote.so
auth            include         system-auth
account         include         system-auth
session         include         system-auth
```

#### Important:
Add the following line one for each username which will user the module
`/etc/sudoers:`
```
Defaults:[username] timestamp_timeout=0
```
This is to ensure sudo checks the PAM everytime a user runs a sudo command

#### Enable the service
```
# systemctl daemon-reload
# systemctl enable --now pam-remote-auth
```


Apache-2.0 © Alexander Hallard <br/>
