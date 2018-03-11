#!/bin/bash
datafile=opt-results.tgz
localdir=../ohmyyeast-data
remotedir=http://sherlockworld.synology.me/share/datasets/yeast/v1
mkdir -p ${localdir}
curl -o ${localdir}/${datafile} ${remotedir}/${datafile}
echo "downloaded: ${localdir}/${datafile}"
cd ${localdir} && tar xf ${datafile} 
