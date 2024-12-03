#!/bin/bash

# 1. Navigate to your Django project directory
cd /home/ayon-ghosh/Desktop/Team/Utopia/Scripts/Utopia

# 2. Activate your virtual environment (uncomment if you're using one)
# source /path/to/your/venv/bin/activate

# 3. Start Django server in the background on all interfaces (0.0.0.0)
nohup python3 manage.py runserver 0.0.0.0:8000 &

# 4. Wait for Django to start (give it a few seconds)
sleep 5

# 5. Run Ngrok and forward traffic from port 8000 to the internet
nohup ngrok http 8000 &

# 6. Update DuckDNS with your current IP address using your DuckDNS script
nohup /home/ayon-ghosh/duckdns/duck.sh &

# 7. Display the final URL for access
echo "Your site is now live at: https://utopia-bd.duckdns.org"
