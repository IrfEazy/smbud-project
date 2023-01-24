#!/usr/bin/fish
# Install the dependencies
sudo echo ""
sudo apt update
sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common

# Add MongoDB GPG Key
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo gpg --dearmor -o /usr/share/keyrings/mongodb-5.0.gpg

# Create a list for MongoDB
echo "deb [arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-5.0.gpg] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-5.0.list

# Update the local package database
sudo apt-get update

# Install the MongoDB with the following command
sudo apt-get --install-recommends install mongodb-org

# Start the MongoDB service and enable it to start automatically after rebooting the system
sudo systemctl start mongod
sudo systemctl enable mongod

# Now, check the status of the MongoDB service
systemctl status mongod

# To verify whether the installation has completed successfully by running the following command
mongosh --eval 'db.runCommand({ connectionStatus: 1 })'
