#!/bin/bash
INPUT=$1
OUTDIR=$2
if [ ! -d "${OUTDIR}" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
    mkdir ${OUTDIR}
fi
while true                                                                                                     
do
echo "Starting job on " `date` >> tranfer_MC2017EXT.log #Date/time of start of job 
echo "Starting job on " `date` #Date/time of start of job 
    for FILE in ${INPUT}/*.root
    do                                                                                                        
	FILESIZE=$(stat -c%s "${FILE}")
	if ((FILESIZE > 0))
	then
            echo "${FILE}" >> tranfer_data2017Full.log
	    #ls -ltrh ${FILE}
	    mv ${FILE} ${OUTDIR}
	fi
    done                                                                                                      
    echo "*********************************************************************************************************************************************************************************************************************************************************************************************" >> tranfer_data2017Full.log
    sleep 1000
done   
