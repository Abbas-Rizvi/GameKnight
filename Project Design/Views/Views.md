# Views

## View 1
> Compute a join of at least three tables.

```SQL
/* Outputs a game with it's ID, Name, Developer, and Rating. */
CREATE OR REPLACE VIEW gamedevrating AS
AS SELECT game.GameID, game.Name, developers.Fname as 'Developer', rating.Rating
FROM game
INNER JOIN developers
ON game.DeveloperID = developers.DeveloperID
INNER JOIN rating
ON rating.GameID = game.GameID
ORDER BY Developer;
```

## View 2
> Use nested queries with the ANY or ALL operator and uses a GROUP BY clause.

```SQL
/* Outputs all fighting games from Nintendo */
CREATE OR REPLACE VIEW nintendoftg AS
SELECT game.GameID, game.Name, developers.Fname AS 'Developer', genre.GName AS 'Genre'  
FROM game 
INNER JOIN developers 
ON game.DeveloperID = developers.DeveloperID 
INNER JOIN genre 
ON genre.GTag = game.Genre
WHERE developers.Fname = ANY(
SELECT DISTINCT Fname 
FROM developers
WHERE DeveloperID = 0) AND game.genre = 'FTG'
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


## View 6
> Show all games and their rating
```SQL
CREATE OR REPLACE VIEW gamerating AS
SELECT game.GameID, game.Name, rating.Rating
FROM game
INNER JOIN rating
ON game.GameID = rating.GameID;
```
