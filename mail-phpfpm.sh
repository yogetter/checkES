#!/bin/sh
template=`cat <<TEMPLATE
***** phpfpm-warning  *****

WARNING signal 6

TEMPLATE
`

/usr/bin/printf "%b" "$template" | mail -s "MOEowncloud phpfpm warning" duncan.c@inwinstack.com jamie.h@inwinstack.com 

