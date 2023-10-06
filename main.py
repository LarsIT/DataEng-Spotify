import subprocess as sp

if __name__ == '__main__':

    try:
        # sp.run(['bash', "scripts/remove_all_old_data.sh"], check=True) # reset data
        # print('data reset') # done

        # sp.run(['bash', "scripts/access_token_script_bash/get_spotify_token.sh"], check=True) # spotify token
        # print('Spotify Token Check') # done

        # sp.run(['bash', "scripts/api_calls/api_call_albums.sh"], check=True) # album call
        # print('Album Call Check') # done

        # sp.run(['python', "data_pipeline/album_modifications/modify_album_data.py"], check=True) # album modification and small script
        # print('Album Modification Check') # done

        # sp.run(['bash', "data_pipeline/album_modifications/extract_album_ids.sh"], check=True) # extract album ids
        # print('AllbumID Extraction Check') # done

        # sp.run(['bash', "data_pipeline/album_modifications/extract_artist_ids.sh"], check=True) # extract artist ids
        # print('ArtistID Extraction Check') # done

        # sp.run(['bash', "scripts/api_calls/api_call_artists.sh"], check=True) # artist call
        # print('Artist Call Check') # done

        sp.run(['bash', "scripts/api_calls/api_call_songs.sh"], check=True) # song call
        print('Song Call Check')


    except sp.CalledProcessError as e:
        print(f'Error: Script execution failed with return code {e.returncode}.')
    # specify order of file execution

    # get_spotify_token.sh

    # api_call_albums.sh

    # modify_album_data.py -> (remove_old_data.sh)

    # extract_album_ids.sh

    # extract_artist_ids.sh

    # api_call.artists.sh

    # api_call.songs.sh