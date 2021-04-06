# simulation-project

make sure git is installed as well as docker and that they are working correctly
then type
`git clone https://github.com/sc-2021-ccu-lanl-statistics/simulation-project.git`
`cd simulation-project`
`docker build . -t batsim:april_9`   This will take some time.
`docker create --name test -it -t batsim:april_9`
`docker start -i test`
`python3 run_simulation.py`
