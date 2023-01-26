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

#MongoDb has no official build for ubuntu 22.04 at the moment.You can force the installation of libssl1.1 by adding the ubuntu 20.04 source, necessary to met the dependencies and install mongod-org:
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt-get update
sudo apt-get install libssl1.1

# Install the MongoDB with the following command
sudo apt-get --install-recommends install mongodb-org

# Start the MongoDB service and enable it to start automatically after rebooting the system
sudo systemctl start mongod
sudo systemctl enable mongod

# Now, check the status of the MongoDB service
systemctl status mongod

# To verify whether the installation has completed successfully by running the following command
mongosh --eval 'db.runCommand({ connectionStatus: 1 })'
