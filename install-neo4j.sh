#!/usr/bin/env bash
# Require sudo rights
sudo echo ""

# Remove Neo4j key
sudo rm /usr/share/keyrings/neo4j.gpg

# Remove latest Neo4j repository from your system's APT sources
sudo rm /etc/apt/sources.list.d/neo4j.list

# Convert the Neo4j key into a format that apt can use to verify downloaded packages
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg

# Add the latest Neo4j repository to your system’s APT sources
echo 'deb [signed-by=/usr/share/keyrings/neo4j.gpg] https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list

# Update your package lists
sudo apt update

# Install the Neo4j package and all of its dependencies
sudo apt-get --install-recommends install neo4j

# Enable Neo4j as a service
sudo systemctl enable neo4j.service

# Start Neo4j as a service
sudo systemctl start neo4j.service

# Print information about the status of Neo4j
neo4j --verbose status
