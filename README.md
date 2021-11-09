This is James Woods take on the best asteroid problem. 
It can handel 2D and 3D data. 
It can graph the results as long as you dont use docker. 
Just add debug to the end of the commands.


Setup

    ./setup.sh


Usage  
   
    to test a data.txt do this
        ./main.py {path/to/data}.txt

    to generate some random data do this
        ./main.py

    to graph the results 

        ./main.py data/data3D.txt debug
        or
        ./main.py data/data2D.txt debug


Docker Stuff

    docker build -t asteroids . 
    docker run -v {path/to/data/}:/app/data/ -it asteroids python3 main.py /app/data/{filename} 

! When using 2d data please disregard the z axis.. !