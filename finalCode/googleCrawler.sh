#!/bin/bash
URL=${@:2}
mkdir -p $1
echo "the Path is" $1;
echo "the Target URL is" $URL;
lynx -dump $URL > $1/gone.tmp
