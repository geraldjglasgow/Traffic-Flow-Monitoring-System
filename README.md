##THINGS TO DO FOR ANALYSIS PROGRAM</br>

##### Browse
* Display cwd and have the ability to change directory's</br>
* Ad hoc asks user for input on data location name</br>
* location names cannot be the same

##### Get Data
* data goes into directory with location as name</br>
* transfer data from the pi to windows comptuer
* data is removed from pi if transfer is fine</br>
* this is repeated for each ad-hoc file transfer</br>
* Cleans the trash out and then moves all .log files to trash</br>

##### Process Data
* trim data so every file has same starting and ending time</br>
* get list of unique mac addresses</br>

* match mac addresses between each location</br>
* separate data by direction of travel
* get total time MAC spent at location</br>
* get last time mac was seen at both locations for total travel time


##### Vendor
* create large list of all unique MAC and vendor lookup</br>
* find % of addresses that are randomized & count of each menu</br>

##### Graph
* Graphs of total MAC detection per minute</br>
* Graph of unique detections per minute
* Graph of matches per minute for each location</br>
* plot locations on google maps map
* let user choose origin
* Plot % of traffic from origin to destination on google maps</br>



### TO-DO LIST
change probemon to this output format:</br>
write current date on startup</br>
HHMMSS,macaddress</br>

10-09-2017 </br>
153613,3231879648f9</br>
153614,0010204160c3</br>
153614,0010204160c3</br>
153614,0010204160c3</br>
153615,1ab947857c45</br>
153606,361288e25796
.</br>
.</br>
.</br>
153623,0010204160c3</br>
153636,1ab947857c45</br>

######reduces characters written to file from 42 to 19. 54% reduction </br>

Packets that need to be written to file can be put in queue, and separate process will put them in file.




