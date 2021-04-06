# simulation-project

make sure git is installed as well as docker and that they are working correctly<br>
then type<br>
`git clone https://github.com/sc-2021-ccu-lanl-statistics/simulation-project.git`<br>
`cd simulation-project`<br>
`docker build . -t batsim:april_9`   This will take some time.<br>
`docker create --name test -it -t batsim:april_9`<br>
`docker start -i test`<br>
`python3 run_simulation.py`<br>
