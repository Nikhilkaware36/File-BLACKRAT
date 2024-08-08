    os.system('figlet -c "TEAM RAT" | lolcat')

def authenticate():
    password = input("Enter the password: ")
    if password == "blackrat":
        print("\033[92mAuthenticating...\033[0m")
        time.sleep(5)
        print("\033[92mAccess Granted! Loading server...\033[0m")
        time.sleep(2)
        print("\n\033[94mDeveloper: Nikhil Kaware\033[0m")
        print("\033[94mGitHub: @Nikhilkaware36\033[0m")
        print("\033[94mInstagram: nikhil.kaware.3\033[0m")
    else:
        print("\033[91mIncorrect password. Access denied.\033[0m")
        exit()

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not os.path.exists('received_files'):
        os.makedirs('received_files')
    file.save(os.path.join('received_files', file.filename))
    return "File received", 200

if __name__ == '__main__':
    show_banner()
    authenticate()
    app.run(host='0.0.0.0', port=5000)