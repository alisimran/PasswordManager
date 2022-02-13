# PYTHON CLI PASSWORD MANAGER 

## Overview
>An offline Password Manager with TUI that stores password securely. This uses 2FA - masterkey (something you know) and OTP (something you have) to authenticate into the vault where the passwords are stored in encrypted format.

>Using the masterkey a vault key is derived using PBKDF2(Password Based Key Derivation Function 2) . The vault key is used to encrypt password using AES (recommended by NIST)


## Clone Project
```bash
# Clone the repository
git clone https://github.com/alisimran/PasswordManager
```
## Install Packages
`pip install -r requirements.txt`

## :information_source: Setup
### Step 2: Set up database
Refer to this article to setup postgresql on your device: https://www.postgresqltutorial.com/install-postgresql/
### Step 3: Connect to database
Enter your username, database name and password inside db_connect.py
### Step 4: Enable 2-step verification
To setup app password(to send otp) refer to this article: https://support.google.com/accounts/answer/185833?hl=en
### Step 3: Generate masterkey
Generate masterhash using function master_hash_gen and place it in masterhash in action.py file


## :information_source: How to Use?
* Enter project direcotry and run main.py `cd project; python main.py`
* Enter required credentials and OTP to enter vault. 
* Press Enter to list menu and navigate accordingly.

## :books: References
https://www.bluespace.tech/blog/evolution-of-password-manager/second-generation-password-manager.html#:~:text=When%20decrypting%20passwords%20from%20vault,than%20generates%20a%20new%20one.)

## Developer
    http://github.com/alisimran

