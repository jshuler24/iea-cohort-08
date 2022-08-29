filename=$1

if test -z $filename; then
    echo "no input given"
else
    test -f $filename || echo "file does not exist"
fi
