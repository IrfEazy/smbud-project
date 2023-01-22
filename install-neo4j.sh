#!/usr/bin/env bash
# Convert the Neo4j key into a format that apt can use to verify downloaded packages
curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg
# Add the Neo4j 4.1 repository to your system’s APT sources
echo "deb [signed-by=/usr/share/keyrings/neo4j.gpg] https://debian.neo4j.com stable 4.1" | sudo tee -a /etc/apt/sources.list.d/neo4j.list
# Update your package lists, and then install the Neo4j package and all of its dependencies
sudo apt update
sudo apt install neo4j
# Enable Neo4j as a service and then start it
sudo systemctl enable neo4j.service
sudo systemctl start neo4j.service
