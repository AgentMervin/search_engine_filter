#remove all [\d+] Cached link gone
echo "test if have read permission"
ls $1
echo "doing real job"

cp $1gone.tmp $1gone
cat $1gone | grep -vP "\[\d+\]Cached" > $1gone.tmp

#get first 100 links
# cat $1gone.tmp| grep -A 100 'Visible links' > $1visiblelinks
cat $1gone.tmp| grep -A 100 'References' > $1visiblelinks
# sed 1d $1visiblelinks| sed 's/[[:digit:]]\+\.//g'| sed 's/ //g' > $1links
cat $1visiblelinks| sed 's/ //g' > $1links


#get titles
cat $1gone.tmp | grep '\[[[:digit:]]*\]' | sed 's/.*\[/\[/g' > $1titles.tmp
#remove google menu
sed -e '1,16d' $1titles.tmp > $1titles
#get abstract
titleNum=$(wc -l $1titles | awk '{print $1}')
echo "" > $1abstracts
for ((counter=1; counter <="$titleNum"; counter++))
do
        titleNo=$(sed -n $counter"p" $1titles | grep -oP '\[\d+\]' | grep -oP '\d+')
        titleNo+="."
        title=$(sed -n $counter"p" $1titles |tr -d '\0' |sed 's/\[[[:digit:]]*\]//g'| tr -d '\0')
        size=${#title}        
        if [ "$size" -gt "2" ]
        then
            tempAbs=$(cat $1gone.tmp | grep -zoP "$title[^\[]*\[" | tr -d '\0')
            size=${#tempAbs}
            if [ "$size" -gt "2" ]
            then
                abstract=$(echo $tempAbs|sed "s/$title//g" | sed "s/\[//g")
                echo $titleNo $abstract >> $1abstracts
                echo "" >> $1abstracts
                echo "" >> $1abstracts
            fi

        fi



done

