-- import database dump
-- lisitng genres and numbers of shows linked to each
SELECT 
    genres.name AS genre, 
    COUNT(tvshows.id) AS number_of_shows
FROM 
    genres
LEFT JOIN 
    tvshows_genres ON genres.id = tvshows_genres.genre_id
LEFT JOIN 
    tvshows ON tvshows.id = tvshows_genres.tvshow_id
GROUP BY 
    genres.name
HAVING 
    number_of_shows > 0
ORDER BY 
    number_of_shows DESC;
