# Spoteamfy Back

This is the backend server for the Spoteamfy application. It is built using Flask, a Python web framework.

## API Endpoints

### `/favorite-tracks`

Returns a list of favorite tracks.

### `/top-artists/<int:num_artists>`

Returns a list of top artists. The `num_artists` parameter specifies the number of artists to retrieve.

### `/top-genres`

Returns a list of top genres.

### `/cluster-genres`

TODO: Implement clustering of genres using AI.

## Running the Server

To run the server, execute the following command:

`python3 -m flask --app main run`
