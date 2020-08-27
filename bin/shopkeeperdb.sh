#!/bin/bash
set -e
# Sanity check command line options
usage() {
    echo "Usage: $0 (create|destroy|reset|dump)"
}

if [ $# -ne 1 ]; then
    usage
    exit 1
fi

# Parse argument. $1 is the first argument
case $1 in
    "create")
        echo "+ sqlite3 var/shopkeeper.sqlite3 < sql/schema.sql"
        sqlite3 var/shopkeeper.sqlite3 < sql/schema.sql
        ;;

    "destroy")
        echo "+ rm -rf var/shopkeeper.sqlite3"
        rm -rf var/shopkeeper.sqlite3
        ;;

    "reset")
        echo "+ rm -rf var/shopkeeper.sqlite3"
        rm -rf var/shopkeeper.sqlite3
        echo "+ sqlite3 var/shopkeeper.sqlite3 < sql/schema.sql"
        sqlite3 var/shopkeeper.sqlite3 < sql/schema.sql
        ;;
    "dump")
        sqlite3 var/shopkeeper.sqlite3 "SELECT * FROM guilds"
        ;;
    *)
        usage
        exit 1
        ;;
esac
