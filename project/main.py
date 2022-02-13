from time import time
from rich import console
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.table import Table
import sqlstatement
import action
import getpass
import db_connect
import generate, secondfactor
from pyfiglet import figlet_format
import time


def start_app(masterkey_given):
    connec = db_connect.connect_db()
    console_obj = console.Console()
    cursor = connec.cursor()
    connec.commit()
    
    cont = True
    
    menu = Table(title='Main Menu', show_lines=True)
    menu.add_column('S.No')
    menu.add_column('Option')
    menu.add_row('1.', 'List All Passwords')
    menu.add_row('2.', 'Add a password')
    menu.add_row('3.', 'Query a password')
    menu.add_row('4.', 'Update password')
    menu.add_row('5.', 'Update username or email')
    menu.add_row('6.', 'Delete password')
    menu.add_row('7.', 'Generate a password')
    
    choices = [str(x) for x in range(8)]
    choices.append('Exit')
    while cont:
        choice = Prompt.ask('Make a choice: {Press Enter for menu}\n\n',
        choices=choices,
        default='0'
        )
        
        if choice == '0':
            console_obj.print(menu, style="white")
            time.sleep(1)
        
        # List all the passwords
        elif choice == '1':
            console_obj.print('List password', style="yellow on black")
            cursor.execute("select * from vault")
            record = cursor.fetchall()
            connec.commit()
            result_table = Table(title='Results')
            result_table.add_column('S.No')
            result_table.add_column('Website')
            result_table.add_column('Username')
            result_table.add_column('Password')
            for i in range(len(record)):
                entry = record[i]
                website = entry[0]
                username = entry[1]
                password = entry[2]
                result_table.add_row(str(i), website, username, password)
            time.sleep(0.3)
            console_obj.print(result_table)
                
        # Add a password
        elif choice == '2':
            console_obj.print('Add password', style="yellow on black")
            website = Prompt.ask("Enter the website")
            username = Prompt.ask("Enter the username")
            plaintext = Prompt.ask("Enter the password")
            password = action.encypt(masterhash, plaintext.encode())
            cursor.execute(sqlstatement.insert_db_vault(), (website, username, password))
            connec.commit()
            console_obj.print("Added successfully", style="green on white")
            
        # Query a password
        elif choice == '3':
            console_obj.print('Search password', style="yellow on black")
            website = Prompt.ask('Enter website to query: ')
            cursor.execute(sqlstatement.select_db_query(), (website,))
            record = cursor.fetchone()
            connec.commit()
            username = record[1]
            password = record[2]
            decrypt_passwd = action.decrypt(masterkey_given, password)
            result_table = Table(title='Results')
            result_table.add_column('S.No')
            result_table.add_column('Website')
            result_table.add_column('Username')
            result_table.add_column('Password')
            result_table.add_row(str(1), website, username, decrypt_passwd)
            console_obj.print(result_table)
            
        # Update a password  
        elif choice == '4':
            console_obj.print('Update password', style="yellow on black")
            website = Prompt.ask("Enter the website")
            plaintext = Prompt.ask("Enter the new password")
            password = action.encypt(masterhash, plaintext.encode())
            cursor.execute(sqlstatement.update_db_password(), (password, website))
            connec.commit()
            console_obj.print("Done!", style="green on white")
        
        # Update username
        elif choice == '5':
            console_obj.print('Update username', style="yellow on black")
            website = Prompt.ask("Enter the website")
            username = Prompt.ask("Enter the new username")
            cursor.execute(sqlstatement.update_db_username(), (username, website))
            connec.commit()
            console_obj.print("Done!", style="green on white")
        
        # Delete password
        elif choice == '6':
             console_obj.print('Delete Password', style="yellow on black")
             website = Prompt.ask("Enter the website")
             cursor.execute(sqlstatement.delete_db_vault(), (website,))
             connec.commit()
             console_obj.print('Deleted Password !', style="green on white")
        elif choice == '7':
            console_obj.print('Generate new Password', style="yellow on black")
            length = ''
            while True:
                l = Prompt.ask("Enter length (recommended atleast 8)")
                if int(l) >= 8:
                    length = length + l
                    break
                else:
                    print("Length entered is less than 8")
            password = generate.generate_password(int(length))
            console_obj.print(f"Generate Password : {password}", style="yellow on black")
        elif choice == 'Exit':
            cont = False
    connec.commit()
    cursor.close()
    
    
    
if __name__ == '__main__':
    masterkey_enc = getpass.getpass("Enter Master Key : ").encode()
    masterhash = action.master_hash_gen(masterkey_enc)
    auth = action.check(masterhash)
    if auth:
        try:
            email = input("Enter your email: ")
            passwd = getpass.getpass("Enter password: ")
            if secondfactor.sendOTP(email, passwd):
                title = figlet_format('Password\nManager' ,font='big') 
                print(f'{title}')
                start_app(masterhash)
            else:
                print("Wrong OTP provided")
        except:
            print(f"[*] Wrong credentials provided.")
            
    else:
        print("Wrong password provided")