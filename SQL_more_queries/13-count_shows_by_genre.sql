-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
WHERE number_of_shows IS NOT NULL;
