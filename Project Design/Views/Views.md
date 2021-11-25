# Views

## View 1
> Compute a join of at least three tables.

```SQL
/* Creates a table with all relevant info, which can be made into smaller views later */
CREATE OR REPLACE VIEW mainview AS
SELECT ga.GameID, ga.Name, ga.ReleaseDate, ga.Price, p.PlatformName AS 'Platform', gr.GName AS 'Genre', dv.Fname AS 'Developer', rt.Rating, mp.Players
FROM game AS ga
INNER JOIN platforms AS p
ON p.PlatformID = ga.PlatformID
INNER JOIN genre AS gr
ON gr.GTag = ga.Genre
INNER JOIN developers AS dv
ON dv.DeveloperID = ga.DeveloperID
INNER JOIN rating AS rt
ON ga.GameID = rt.GameID
INNER JOIN multiplayer AS mp
ON ga.GameID = mp.GameID
ORDER BY GameID;
```

## View 2
> Use nested queries with the ANY or ALL operator and uses a GROUP BY clause.

```SQL
/* Outputs all fighting games from dev 0 */
CREATE OR REPLACE VIEW dev0ftg AS
SELECT game.GameID, game.Name, developers.Fname AS 'Developer', genre.GName AS 'Genre'  
FROM game 
INNER JOIN developers 
ON game.DeveloperID = developers.DeveloperID 
INNER JOIN genre 
ON genre.GTag = game.Genre
WHERE developers.Fname = ANY(
    SELECT DISTINCT Fname 
    FROM developers
    WHERE DeveloperID = 0) 
AND game.genre = 'FTG'
GROUP BY GameID;
```

## View 3

> Use a correlated nested query

```SQL
/* Outputs all games that have a rating greater than the average */
CREATE OR REPLACE VIEW topratedgames AS
SELECT * FROM(
    SELECT game.GameID, game.Name, rating.Rating
    FROM game
    INNER JOIN rating
    ON game.GameID = rating.GameID) 
AS gr
WHERE gr.Rating > ( 
    SELECT AVG(Rating)
    FROM gamerating);
```

## View 4
> Use a Full Join
```SQL
/* Outputs all games, with multiplayer information, equivalent to FULL JOIN as MariaDB doesn't like it */
CREATE OR REPLACE VIEW gamesplayercount AS
SELECT * FROM game 
LEFT JOIN multiplayer 
ON game.GameID = multiplayer.GameID 
UNION 
SELECT * 
FROM game 
RIGHT JOIN multiplayer 
ON game.GameID = multiplayer.GameID;
```

## View 5
> Use a nested query with any of the set operations UNION, EXCEPT, or INTERSECT
```SQL
/* Outputs games on platform0 and that are Adventure */
CREATE OR REPLACE VIEW plat0adv AS
SELECT ga.GameID, ga.Name
FROM
(
    SELECT game.GameID, game.Name , genre.GTag
    FROM game
    INNER JOIN genre
    WHERE game.Genre = genre.GTag
)
AS ga
WHERE ga.GTag = 'ADV'
INTERSECT
SELECT game.GameID, game.Name 
FROM game
INNER JOIN platforms 
ON game.PlatformID = platforms.PlatformID
WHERE platforms.PlatformID = 0;
```

## View 6
```SQL
/* Show all games and their rating */
CREATE OR REPLACE VIEW gamerating AS
SELECT game.GameID, game.Name, rating.Rating
FROM game
INNER JOIN rating
ON game.GameID = rating.GameID;
```

## View 7
```SQL
/* Outputs list of games that are multiplayer, and from the 1980's */
CREATE OR REPLACE VIEW multiplayer80s
SELECT g.GameID, g.Name, g.ReleaseDate, p.PlatformName, f.Players
FROM game AS g
INNER JOIN platforms AS p
ON p.PlatformID = g.PlatformID
INNER JOIN (
    SELECT g.GameID, g.ReleaseDate, m.Players
    FROM game AS g
    INNER JOIN multiplayer AS m
    ON m.GameID = g.GameID) 
AS f
ON g.GameID = f.GameID
WHERE f.ReleaseDate <= 1999 AND f.ReleaseDate >= 1980 AND f.Players > 1;
```

## View 8
```SQL
/* Outputs a game with it's ID, Name, Developer, and Rating. */
CREATE OR REPLACE VIEW gamedevrating AS
SELECT game.GameID, game.Name, developers.Fname as 'Developer', rating.Rating
FROM game
INNER JOIN developers
ON game.DeveloperID = developers.DeveloperID
INNER JOIN rating
ON rating.GameID = game.GameID
ORDER BY Developer;
```

## View 9
```SQL
/* Outputs all games, and orders by Platform and multiplayer */
SELECT ga.GameID, ga.Name, ga.ReleaseDate, ga.Price, p.PlatformName AS 'Platform', gr.GName AS 'Genre', dv.Fname AS 'Developer', rt.Rating, mp.Players
FROM game AS ga
INNER JOIN platforms AS p
ON p.PlatformID = ga.PlatformID
INNER JOIN genre AS gr
ON gr.GTag = ga.Genre
INNER JOIN developers AS dv
ON dv.DeveloperID = ga.DeveloperID
INNER JOIN rating AS rt
ON ga.GameID = rt.GameID
INNER JOIN multiplayer AS mp
ON ga.GameID = mp.GameID
ORDER BY Platform AND Players;
```

## View 10
```SQL
/* Outputs all dev0 games from the 90's */
CREATE OR REPLACE VIEW dev090s
SELECT g.GameID, g.Name, g.ReleaseDate, dv.Fname AS 'Developer', f.Players
FROM game AS g
INNER JOIN developers AS dv
ON dv.DeveloperID = g.DeveloperID
INNER JOIN (
    SELECT g.GameID, g.ReleaseDate, m.Players
    FROM game AS g
    INNER JOIN multiplayer AS m
    ON m.GameID = g.GameID) 
AS f
ON g.GameID = f.GameID
WHERE f.ReleaseDate <= 1999 AND f.ReleaseDate >= 1990 AND f.Players > 1;
```
