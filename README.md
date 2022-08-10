Test task for Starnavi.

<b>Basic Features:</b> \
● user signup \
● user login \
● post creation \
● post like \
● post unlike \
● analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
aggregated by day.\
● user activity an endpoint which will show when user was login last time and when he
mades a last request to the service.\


JWT token authentication


<b>Steps to install:<b>\
● `clone repository`\
● create `.env` file copying everything from `.env.example`\
● in terminal `docker-compose up` to run docker container and project \
● in another terminal window `docker compose exec web python manage.py migrate` to migrate \
● visit `http://127.0.0.1:8000/api/schema/swagger-ui/` to learn project's docs and make simple actions
 
