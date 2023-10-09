import subprocess as sp

if __name__ == '__main__':

    try:
        # # Data reset
        # sp.run(['bash', "scripts/remove_all_old_data.sh"], check=True)
        # print('data reset') 

        # # Get Access Token
        # sp.run(['bash', "scripts/access_token_script_bash/get_spotify_token.sh"], check=True) 
        # print('Spotify Token Check')

        # # API Call Albums

        # sp.run(['bash', "scripts/api_calls/api_call_albums.sh"], check=True) 
        # print('Album Call Check') 

        # sp.run(['python', "data_pipeline/album_modifications/modify_album_data.py"], check=True) # album modification and small script
        # print('Album Modification Check') 

        # sp.run(['bash', "data_pipeline/album_modifications/extract_album_ids.sh"], check=True) # extract album ids
        # print('AllbumID Extraction Check') 

        # sp.run(['bash', "data_pipeline/album_modifications/extract_artist_ids.sh"], check=True) # extract artist ids
        # print('ArtistID Extraction Check') 

        # # API Call Artists
        # sp.run(['bash', "scripts/api_calls/api_call_artists.sh"], check=True) # artist call
        # print('Artist Call Check') 

        # sp.run(['python', "data_pipeline/artist_modifications/modify_artist_data.py"], check=True) # artist call
        # print('Artist Modification Check') 

        # API Call Songs
        sp.run(['bash', "scripts/api_calls/api_call_songs.sh"], check=True) # song call
        print('Song Call Check') # done

        sp.run(['python', "data_pipeline/song_modifications/modify_song_data.py"], check=True) # artist call
        print('Song Modification Check') 

        # data transformation
        sp.run(['python', "data_pipeline/data_transformation/albums_artists.py"], check=True) # artist call
        print('Albums_Artists Transformation Check') 

        sp.run(['python', "data_pipeline/data_transformation/artists_genres.py"], check=True) # artist call
        print('Artist_Genres Transformation Check') 

        sp.run(['python', "data_pipeline/data_transformation/songs_albums.py"], check=True) # artist call
        print('Song_Albums Transformation Check') 
        


    except sp.CalledProcessError as e:
        print(f'Error: Script execution failed with return code {e.returncode}.')
