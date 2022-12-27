from datetime import datetime

with open("github_action/update_date.txt","w") as text_file:
    text_file.write(f'This repo is update on {datetime.now()}')
