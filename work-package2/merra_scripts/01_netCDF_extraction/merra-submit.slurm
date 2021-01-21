#!/bin/bash
#SBATCH --ntasks=2
#SBATCH --job-name=tideGauge
#SBATCH --time=00-00:10:00
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out


STARTDIR=`pwd`

#Select File to run
export file="$SLURM_ARRAY_TASK_ID-tideGauge.py"
export args=""

#Select how logs get stored
mkdir $SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID
export debug_logs="$SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID/job_$SLURM_JOB_ID.log"
export benchmark_logs="$SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID/job_$SLURM_JOB_ID.log"

## Load Modules
module load anaconda/anaconda3
source activate netcdf4-local

## Enter Working Directory ##
cd $SLURM_SUBMIT_DIR
## Create Log File ##
echo $SLURM_SUBMIT_DIR
echo "JobID: $SLURM_JOB_ID" >> $debug_logs
echo "Running on $SLURM_NODELIST" >> $debug_logs
echo "Running on $SLURM_NNODES nodes." >> $debug_logs
echo "Running on $SLURM_NPROCS processors." >> $debug_logs
echo  "Current working directory is `pwd`" >> $debug_logs

## Module debugging ##
module list >> $debug_logs
which mpirun >> $debug_logs

date >> $benchmark_logs
echo "ulimit -l: " >> $benchmark_logs
ulimit -l >> $benchmark_logs

## Run job ##
echo "Running $file" >> job.${SLURM_JOB_ID}.out
python -u $file $args >> job.${SLURM_JOB_ID}.out
sleep 3

date >> $benchmark_logs
echo "ulimit -l" >> $benchmark_logs
ulimit -l >> $benchmark_logs

## Compress files ##
cd /home/`whoami`/merraLocalized/

# Get the directory -- regex match the array ID
DIR_TO_COMP=`ls | grep -E "^${SLURM_ARRAY_TASK_ID}-"`
echo "Compressing directory ${DIR_TO_COMP}" >> ${STARTDIR}/job.${SLURM_JOB_ID}.out

tar czvf ${DIR_TO_COMP}.tar.gz ${DIR_TO_COMP}

# Delete no longer needed files
echo "${DIR_TO_COMP}.tar.gz done... deleting ${DIR_TO_COMP}" >> ${STARTDIR}/job.${SLURM_JOB_ID}.out

rm -rfv ${DIR_TO_COMP}


## Directory Cleanup ##
cd ${STARTDIR}
mv job.${SLURM_JOB_ID}.err $SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID/
mv job.${SLURM_JOB_ID}.out $SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID/
