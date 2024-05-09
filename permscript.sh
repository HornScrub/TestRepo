#!/bin/bash
# Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

# Create a new bash script that performs the following:

# Prompts user for input directory path or file.

echo "Enter the directory path or file you want to change permissions for: "
read path

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777, 775, 664)

echo "Enter the input permissions number (e.g. 777 to perform a chmod 777, 775, 664, etc.): "
read perm

# Make sure the path is valid

if [ ! -d "$path" ] && [ ! -f "$path" ]; then
    echo "$path is not a directory or file!"
    exit 1
fi

# Navigates to the directory input by the user and changes all files inside it to the input setting.

cd "$path"
chmod "$perm" *

# Prints to the screen the directory contents and the new permissions settings of everything in the directory or file you selected.
if [ -d "$path" ]; then
    echo "Here are the new permission settings for all the files inside $path:"
else
    echo "Here are the new permission settings for $path:"
fi

ls -l