# Mixtape

## Prerequisites

* Python 2.7
* Python library
    * argparse 
    * pytest

## Using the tool
1. Clone the code and install the required packages:

        git clone https://github.com/mong2/mixtape.git
        cd mixtape
2. Mixtape Application includes below actions, 
   *  Remove an existing playlist.
        * action: "delete"
        * required params: 
            * playlist_id (integer)
   * Add an existing song to an existing playlist.
        * action: "update"
        * required params: 
            * playlist_id (integer)
            * song_id (integer)
   * Add a new playlist for an existing user; the playlist should contain at least one existing song.
        * action: "create"
        * required params:
            * user_id (integer)
            * song_id (integer or array of integers)
2. Example of the changefile. Note: changefile should be in valid JSON format. 
   ```
   {
       "changes": [
            {
                "action": "delete",
                "playlist_id": 4
            },
            {
                "action": "update",
                "playlist_id": 5,
                "song_id": 3
           }
       ]
   }
   ```
3. run the application. Note: Please make sure to specify a valid file path for the files. Mixtape currently does not support writing files to a non-existing working directory.
    ```
    python mixtape.py mixtape.json changefile.json output.json
    ```

### Scale
Mixtape is currently reading json files and store it as memories. The method may eventually cuases application failure due to machine running out of memories. Two ideas i have in mind to reduce the memory issue. First is to stream the data. To perform streaming data alone will not be affective due to the structure of the input file. The application is required to read the whole file to determine the existing users, playlists and songs so that it can determine whether it has the data to perform any requested action. With a database on the side, the application can stream the data and ingest the data from the input file to create a full view of the existing data. The application then can stream the change file and make changes accordingly. Another way is to utilize a library called Pandas in Python. Pandas is designed to read large files that contains millions of data. The application can read in the input file using Pandas to build a full view of exisitng data. The application then can stream the change file and make changes accordingly. 
