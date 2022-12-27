from datetime import datetime

with open("update_date.txt","w") as text_file:
    text_file.write(f"The file is updated on {datetime.now()}")
