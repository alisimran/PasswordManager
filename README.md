# PYTHON CLI PASSWORD MANAGER 

##Overview
>An offline Password Manager that stores password securely. This uses 2FA - masterkey (something you know) and OTP (something you have) to authenticate into the vault where the passwords are stored in encrypted format.

Using the masterkey a vault key is derived using PBKDF2(Password Based Key Derivation Function 2) . The vault key is used to encrypt password using AES (recommended by NIST)

## Install Packages
`pip install -r requirements.txt`

## :information_source: Setup
### Step 1: Clone Project
```bash
# Clone the repository
git clone 
# Enter project and run
python main.py
```
### Step 2: Set up database
Refer to this article to setup postgresql on your device
### Step 3: Connect to database
Enter your username, database name and password inside db_connect.py
### Step 4: Enable 2-step verification
To setup app password(to send otp) refer to this article: https://support.google.com/accounts/answer/185833?hl=en
### Step 3: Generate masterkey
Generate masterhash using function master_hash_gen and place it in masterhash in action.py file


## :information_source: How to Use?

## Developer
    http://github.com/alisimran

