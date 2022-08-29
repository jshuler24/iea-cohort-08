#!/bin/bash
# check input
if [[ -z "${1:-}" ]]; then
   printf "Nothing specified.  Include a filename as an argument.\n"
fi
# Take any number ofarguments
# Report that filename does not exist
# Remove files that are empty
# Mark non-empty files as inpsecte
for files in "$@"; do
   if [[ ! -e "$files" ]]; then
      printf "Filename '%s$files' does not exist.\n"
   elif [[ ! -s $files ]]; then
      printf "Filename '%s$files' is an empty file and has been removed.\n"
      rm "$files"
   else 
      printf "Filename '%s$files' exists and has been inspected.\n"
      printf "\nInspected by Josh\n" >> "$files"
   fi
done