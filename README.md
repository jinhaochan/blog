# Blog backend stuff

## Local activities

Write your post in mark down format in `content`

Navigate to the root folder and run `pelican`. This should generate the HTML assets under `output`

Push the changes up to master and you're done!

## Testing remotely

In the Procfile, change the dynamic variable `$PORT` to a concrete one e.g. `8080`. The dynamic port is meant for Heroku to assign a port number to it
