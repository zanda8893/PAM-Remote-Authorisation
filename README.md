# PAM Remote Authorisation

The PAM Remote Authorization project facilitates secure execution of sudo commands by leveraging a Discord bot for authorization. This system operates by allowing pre-approved users to gain authorization by reacting to a specific message indicating the user and command they intend to execute.

## Features

- **Discord Bot Integration:** Utilizes a Discord bot for seamless authorization.
- **Sudo Command Execution:** Allows authorized users to execute sudo commands.
- **User Approval Mechanism:** Users gain authorization by reacting to a designated message.
- **Secure Authorization:** Ensures execution privileges only to approved users.

## How It Works

1. **Discord Bot Setup:** Integrate the bot into your Discord server.
2. **Authorization Process:** Users react to the authorization message with a 👍.
3. **Execution:** Approved users can execute sudo commands.

## Getting Started

Follow these steps to get started with PAM Remote Authorization:

1. Clone the repository.
2. Configure the Discord bot and authentication settings.
3. Run the application and start granting authorization to approved users.

## Requirements

- Python 3.11
- gcc
- Discord bot

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

### Bot setup

Currently, the bot sends messages to a channel called "approval". Users to authorise commands must have the role "approvers".
<br/>You must create this channel and role.

Place your discord token in the config

`/etc/remote_auth.conf:`
```
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

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests.

Apache-2.0 © Alexander Hallard
