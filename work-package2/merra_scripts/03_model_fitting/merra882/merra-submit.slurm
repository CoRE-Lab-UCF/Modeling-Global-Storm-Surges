#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --job-name=tideGauge
#SBATCH --time=00-08:00:00
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
pip install -U scikit-learn
pip install scipy


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

## Directory Cleanup ##
cd ${STARTDIR}
mv job.${SLURM_JOB_ID}.err $SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID/
mv job.${SLURM_JOB_ID}.out $SLURM_JOB_ID-$SLURM_ARRAY_TASK_ID/
