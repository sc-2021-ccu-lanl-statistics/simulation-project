def getStrings():
    grizzly_workload = """
    
    grizzly-workload:{ 
        option:value,
        option:value,
        ...
    }
    
    Required:

        "time": "STR"                               Where STR is the amount of time to include in the
                                                    workload.  The format of this quoted string is:
                                                    :                                   all data
                                                    Month-Day-Year:                     from this date until end
                                                    :Month-Day-Year                     from start until this date
                                                    Month-Day-Year : Month-Day-Year     from this date to this date
        
        "input": "PATH"                             Where PATH is location of jobs csv file (sanitized or not)

    Optional:
        "number-of-jobs": INT                       The number of jobs wanted from the start.If negative,
                                                    it is the amount
                                                    of jobs from the end going backward.If not specified,
                                                    all jobs in the time range are included.
                                                    required for --random-selection

        "scale-widths-based-on": INT                change the widths of jobs based on:
                                                    'new_width = old_width * --nodes/INT'
                                                    where old_width is what the input is based on
                                                    Since grizzly data is based on 1490 nodes
                                                    this is typically the value for INT
         
              
        "random-selection":true|false               To get a random selection of jobs

        "submission-time": <FLOAT><:exp|fixed>      This dictates the time between submissions and what kind of randomness.
                           <FLOAT:FLOAT:unif>       If zero is used for a float,combined with ":fixed" then all jobs will start at time zero.
                                                    If omitted, grizzly data will be used.
                                                            
                                                    exp: This will be exponentially distributed, random values with mean time between submissions to be FLOAT.
                                                    fixed: All jobs will have this time between them unless zero is used for a FLOAT.
                                                    unif: This will be uniform, random values from min:max
                                                    ex:     
                                                            "submission-time": "200.0:exp"
                                                            "submission-time": "100.0:fixed"
                                                            "submission-time": "0.0:fixed"
                                                            "submission-time": "0:200.0:unif"

        "wallclock-limit":<FLOAT|INT%|STR>          wallclock limits will all be set to this for FLOAT. (-1) means the value will not be used in Batsim.
                                                    wallclock limits will be a % of run time for INT%
                                                    wallclock limits will be random from min % of runtime to max % in STR format '"min%:max%"'
                                                    wallclock limits will be random seconds from min to max in STR format  '"min:max"'
                                                    wallclock limits will be what the grizzly data is if not set.
                                                    ex:     "wallclock-limit": -1
                                                            "wallclock-limit": 500.3
                                                            "wallclock-limit": 101%
                                                            "wallclock-limit": "50%:150%"
                                                            "wallclock-limit": "100:3000"
        "read-time": <FLOAT|INT%|"STR">             set this fixed time to readtime in seconds for FLOAT.
                                                    set this to % of run time for INT%.
                                                    set this to random % of run time for STR format "min%:max%"
                                                    set this to random seconds from min to max in STR format   "min:max".
                                                    readtime will be omitted in the workload if not included.
                                                    ex:     "read-time": 20
                                                            "read-time": 2%
                                                            "read-time": "2%:4%"
                                                            "read-time": "2:20"

        "dump-time": <FLOAT|INT%|"STR">             set this fixed time to dumptime in seconds for FLOAT.
                                                    set this to % of run time for INT%.
                                                    set this to random % of run time for STR format "min%:max%"
                                                    set this to random seconds from min to max in STR format   "min:max".
                                                    dumptime will be omitted in the workload if not included.
                                                    ex:     "dump-time": 20
                                                            "dump-time": 3%
                                                            "dump-time": "3%:5%"
                                                            "dump-time": "3:30"

        "checkpoint-interval": <FLOAT|INT%|"STR">   set this fixed time to checkpoint in seconds for FLOAT.
                                                    set this to % of run time for INT%.
                                                    set this to random % of run time for STR format "min%:max%"
                                                    set this to random seconds from min to max in STR format   "min:max".
                                                    checkpoint will be omitted in the workload if not included.
                                                    ex:     "checkpoint-interval": 120
                                                            "checkpoint-interval": 30%
                                                            "checkpoint-interval": "10%:30%"
                                                            "checkpoint-interval": "120:240"
    

    """
    synthetic_workload="""
        "synthetic-workload":{
            "option":value,
            "option":value,
            ...
        }
Required Options 1:
    --file FILE                                     Options will come from a json file.

Required Options 2:
    number-of-jobs: <INT>                           total number of jobs in this workload
    
    nodes: <INT>                                    total number of nodes in this cluster for this workload

    number-of-resources:  <INT:fixed>               This dictates the number of resources used for each job and the kind of randomness.
                          <INT:INT:unif>            INT must be > 0
                          <FLOAT:FLOAT:norm>
                          <STR:pos:csv>      
                                                    fixed: All jobs will have INT for number of resources.
                                                    csv: Will come from file at STR.  pos is the position in each row that holds resources. 0 is first column.
                                                    unif: This will be uniform, random values from min:max
                                                    variations of min:max include:
                                                            :		    1 to the total amount of resources
                                                            min:		min to the total amount of resources
                                                            :max		1 to max
                                                            min:max		min to max
                                                    ex:     
                                                            'number-of-resources: "50:fixed"'
                                                            'number-of-resources: "::unif"'
                                                            'number-of-resources: "2::unif"'
                                                            'number-of-resources: ":10:unif"'
                                                            'number-of-resources: "2:10:unif"'
                                                            'number-of-resources: "~/500000.csv:0:csv"'

    
    duration-time:  <FLOAT><:exp|fixed>             This dictates the duration times and what kind of randomness. FLOAT must be > 0.
                    <FLOAT:FLOAT:unif>
                    <FLOAT:FLOAT:norm>      
                    <STR:pos:time:csv>              exp: This will be exponentially distributed, random values with mean time of durations to be FLOAT.
                                                    fixed: All jobs will have FLOAT for a duration.
                                                    csv: Will come from file at STR.  pos is the position in each row that holds resources. 0 is first column. h|m|s for time.hour|minute|second
                                                    unif: This will be uniform, random values from min:max
                                                    ex:     
                                                            'duration-time: "200.0:exp"'
                                                            'duration-time: "100.0:fixed"
                                                            'duration-time: "0:200.0:unif"'
                                                            'duration-time: "~/500000.csv:1:h:csv"'
                
    submission-time:  <FLOAT><:exp|fixed>           This dictates the time between submissions and what kind of randomness.
                      <FLOAT:FLOAT:unif>            If zero is used for a float,combined with ":fixed" then all jobs will start at time zero.
                      <FLOAT:FLOAT:norm>
                                                            
                                                    exp: This will be exponentially distributed, random values with mean time between submissions to be FLOAT.
                                                    fixed: All jobs will have this time between them unless zero is used for a FLOAT.
                                                    unif: This will be uniform, random values from min:max
                                                    ex:     
                                                            'submission-time: "200.0:exp"'
                                                            'submission-time: "100.0:fixed"'
                                                            'submission-time: "0.0:fixed"'
                                                            'submission-time: "0:200.0:unif"'
Optional Options:
                                                                                            
    wallclock-limit: <FLOAT|INT%|STR>               wallclock limits will all be set to this for FLOAT. (-1) means the value will not be used in Batsim.
                                                    wallclock limits will be a % of run time for INT%
                                                    wallclock limits will be random from min % of runtime to max % in STR format '"min%:max%"'
                                                    wallclock limits will be random seconds from min to max in STR format  '"min:max"'
                                                    wallclock limits will be -1 if not set
                                                    ex:     'wallclock-limit: -1'
                                                            'wallclock-limit: 500.3'
                                                            'wallclock-limit: 101%'
                                                            'wallclock-limit: "50%:150%"'
                                                            'wallclock-limit: "100:3000"'

    read-time: <FLOAT|INT%|STR>                     set this fixed time to readtime in seconds for FLOAT.
                                                    set this to % of run time for INT%.
                                                    set this to random % of run time for STR format "min%:max%"
                                                    set this to random seconds from min to max in STR format   "min:max".
                                                    readtime will be omitted in the workload if not included.
                                                    ex:     'read-time: 20'
                                                            'read-time: 2%'
                                                            'read-time: "2%:4%"'
                                                            'read-time: "2:20"'

    dump-time: <FLOAT|INT%|STR>                     set this fixed time to dumptime in seconds for FLOAT.
                                                    set this to % of run time for INT%.
                                                    set this to random % of run time for STR format "min%:max%"
                                                    set this to random seconds from min to max in STR format   "min:max".
                                                    dumptime will be omitted in the workload if not included.
                                                    ex:     'dump-time: 20'
                                                            'dump-time: 3%'
                                                            'dump-time: "3%:5%"'
                                                            'dump-time: "3:30"'

    checkpoint-interval: <FLOAT|INT%|STR>           set this fixed time to checkpoint in seconds for FLOAT.
                                                    set this to % of run time for INT%.
                                                    set this to random % of run time for STR format "min%:max%"
                                                    set this to random seconds from min to max in STR format   "min:max".
                                                    checkpoint will be omitted in the workload if not included.
                                                    ex:     'checkpoint-interval: 120'
                                                            'checkpoint-interval: 30%'
                                                            'checkpoint-interval: "10%:30%"'
                                                            'checkpoint-interval: "120:240"'

    """

    output="""
        "output":{
            option:value,
            option:value,
            ...
        }

        "AAE":true                                  whether you want the average application efficiency computed

        "makespan":true|false                       whether you want the makespan computed in output
                                                    not to be used in conjunction with avg-makespan

        "avg-makespan":INT                          whether you want an average makespan.  If so, how
                                                    many times do you want each experiment to Run to make
                                                    an average of?  Enter that in INT

        "raw":INT                                   whether to output raw post processing data
                                                    raw = 1,debug=2, raw and debug=3


    """
    node_sweep="""

    """
    smtbf_sweep="""

    """
    checkpoint_sweep="""

    """
    performance_sweep="""

    """
    general="""

    """
    sweeps="""

    """
    options="""

    """
    return {"grizzly-workload":grizzly_workload,"synthetic-workload":synthetic_workload,
        "output":output,"node-sweep":node_sweep,"SMTBF-sweep":smtbf_sweep,"checkpoint-sweep":checkpoint_sweep,"performance-sweep":performance_sweep,"general":general,"sweeps":sweeps,"options":options}

