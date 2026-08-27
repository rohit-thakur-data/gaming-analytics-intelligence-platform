USE gaming_analytics_db;

-- =========================================
-- Question 1: Players by Game Genre
-- =========================================

SELECT
    GameGenre,
    COUNT(*) AS TotalPlayers
FROM player_statistics
GROUP BY GameGenre
ORDER BY TotalPlayers DESC;

-- =========================================
-- Question 2: Players by Location
-- =========================================

SELECT
    Location,
    COUNT(*) AS TotalPlayers
FROM player_statistics
GROUP BY Location
ORDER BY TotalPlayers DESC;

-- =========================================
-- Question 3: Players by Engagement Level
-- =========================================

SELECT
    EngagementLevel,
    COUNT(*) AS TotalPlayers
FROM player_statistics
GROUP BY EngagementLevel
ORDER BY TotalPlayers DESC;

-- =========================================
-- Question 4: Players by Gender
-- =========================================

SELECT
    Gender,
    COUNT(*) AS TotalPlayers
FROM player_statistics
GROUP BY Gender
ORDER BY TotalPlayers DESC;

-- =========================================
-- Question 5: Average Player Age
-- =========================================

SELECT
    ROUND(AVG(Age), 2) AS AverageAge
FROM player_statistics;

-- =========================================
-- Question 6: Average Playtime
-- =========================================

SELECT
    ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM player_statistics;

-- =========================================
-- Question 7: Average Sessions Per Week
-- =========================================

SELECT
    ROUND(AVG(SessionsPerWeek), 2) AS AverageSessionsPerWeek
FROM player_statistics;

-- =========================================
-- Question 8: Average Player Level
-- =========================================

SELECT
    ROUND(AVG(PlayerLevel), 2) AS AveragePlayerLevel
FROM player_statistics;

-- =========================================
-- Practice: Average Female Player Age
-- =========================================

SELECT
    ROUND(AVG(Age), 2) AS AverageFemaleAge
FROM player_statistics
WHERE Gender = 'Female';

-- =========================================
-- Question 9: Purchasing Players
-- =========================================

SELECT
    SUM(InGamePurchases) AS PurchasingPlayers
FROM player_statistics;

-- =========================================
-- Question 10: Overall Purchase Rate
-- =========================================

SELECT
    ROUND(
        SUM(InGamePurchases) / COUNT(*) * 100,
        2
    ) AS PurchaseRate
FROM player_statistics;

-- =========================================
-- Question 11: Purchase Rate by Game Genre
-- =========================================

SELECT
    GameGenre,
    ROUND(
        AVG(InGamePurchases) * 100,
        2
    ) AS PurchaseRate
FROM player_statistics
GROUP BY GameGenre
ORDER BY PurchaseRate DESC;

-- =========================================
-- Question 12: Non-Purchasing Players
-- =========================================

SELECT
    COUNT(*) - SUM(InGamePurchases)
        AS NonPurchasingPlayers
FROM player_statistics;

-- =========================================
-- Question 13: High Engagement Players
-- =========================================

SELECT
    COUNT(*) AS HighEngagementPlayers
FROM player_statistics
WHERE EngagementLevel = 'High';

-- =========================================
-- Question 14: Players from India
-- =========================================

SELECT
    COUNT(*) AS IndianPlayers
FROM player_statistics
WHERE Location = 'India';

-- =========================================
-- Question 15: Female Players from India
-- =========================================

SELECT
    COUNT(*) AS FemaleIndianPlayers
FROM player_statistics
WHERE Gender = 'Female'
AND Location = 'India';

-- =========================================
-- Question 16: Players from India or USA
-- =========================================

SELECT
    COUNT(*) AS IndiaOrUSAPlayers
FROM player_statistics
WHERE Location = 'India'
OR Location = 'USA';

-- =========================================
-- Question 17: Players Age 25 or Older
-- =========================================

SELECT
    COUNT(*) AS PlayersAge25Plus
FROM player_statistics
WHERE Age >= 25;

-- =========================================
-- Question 18: Average Playtime of High Engagement Players
-- =========================================

SELECT
    ROUND(AVG(PlayTimeHours), 2)
        AS AverageHighEngagementPlaytime
FROM player_statistics
WHERE EngagementLevel = 'High';

-- =========================================
-- Question 19: Average Playtime by Genre
-- =========================================

SELECT
    GameGenre,
    ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM player_statistics
GROUP BY GameGenre
ORDER BY AveragePlaytime DESC;

-- =========================================
-- Question 20: Average Playtime by Engagement
-- =========================================

SELECT
    EngagementLevel,
    ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM player_statistics
GROUP BY EngagementLevel
ORDER BY AveragePlaytime DESC;

-- =========================================
-- Question 21: Average Player Level by Genre
-- =========================================

SELECT
    GameGenre,
    ROUND(AVG(PlayerLevel), 2) AS AveragePlayerLevel
FROM player_statistics
GROUP BY GameGenre
ORDER BY AveragePlayerLevel DESC;

-- =========================================
-- Question 22: Average Sessions by Engagement
-- =========================================

SELECT
    EngagementLevel,
    ROUND(AVG(SessionsPerWeek), 2) AS AverageSessions
FROM player_statistics
GROUP BY EngagementLevel
ORDER BY AverageSessions DESC;

-- =========================================
-- Question 23: High Engagement Playtime by Genre
-- =========================================

SELECT
    GameGenre,
    ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM player_statistics
WHERE EngagementLevel = 'High'
GROUP BY GameGenre
ORDER BY AveragePlaytime DESC;

-- =========================================
-- Question 24: Genres with More Than 8,000 Players
-- =========================================

SELECT
    GameGenre,
    COUNT(*) AS TotalPlayers
FROM player_statistics
GROUP BY GameGenre
HAVING COUNT(*) > 8000
ORDER BY TotalPlayers DESC;

-- =========================================
-- Question 25: Genres with Average Playtime > 12
-- =========================================

SELECT
    GameGenre,
    ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM player_statistics
GROUP BY GameGenre
HAVING AVG(PlayTimeHours) > 12
ORDER BY AveragePlaytime DESC;

-- =========================================
-- Question 26: Large Genres Among High Engagement Players
-- =========================================

SELECT
    GameGenre,
    COUNT(*) AS TotalPlayers
FROM player_statistics
WHERE EngagementLevel = 'High'
GROUP BY GameGenre
HAVING COUNT(*) > 2000
ORDER BY TotalPlayers DESC;

-- =========================================
-- SQL MINI BUSINESS ANALYSIS
-- =========================================

-- =========================================
-- Mini Analysis 1:
-- Player Count by Genre
-- =========================================

SELECT
    GameGenre,
    COUNT(*) AS TotalPlayers
FROM player_statistics
GROUP BY GameGenre
ORDER BY TotalPlayers DESC;

-- =========================================
-- Mini Analysis 2:
-- Average Playtime by Genre
-- =========================================

SELECT
    GameGenre,
    ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM player_statistics
GROUP BY GameGenre
ORDER BY AveragePlaytime DESC;

-- =========================================
-- Mini Analysis 3:
-- Purchase Rate by Genre
-- =========================================

SELECT
    GameGenre,
    ROUND(AVG(InGamePurchases) * 100, 2) AS PurchaseRate
FROM player_statistics
GROUP BY GameGenre
ORDER BY PurchaseRate DESC;

-- =========================================
-- Mini Analysis 4:
-- Genre Performance Summary
-- =========================================

SELECT
    GameGenre,

    COUNT(*) AS TotalPlayers,

    ROUND(AVG(PlayTimeHours), 2)
        AS AveragePlaytime,

    ROUND(AVG(InGamePurchases) * 100, 2)
        AS PurchaseRate

FROM player_statistics

GROUP BY GameGenre

ORDER BY TotalPlayers DESC;

-- =========================================
-- Mini Analysis 5:
-- Engagement Performance Summary
-- =========================================

SELECT
    EngagementLevel,

    COUNT(*) AS TotalPlayers,

    ROUND(AVG(PlayTimeHours), 2)
        AS AveragePlaytime,

    ROUND(AVG(SessionsPerWeek), 2)
        AS AverageSessions,

    ROUND(AVG(InGamePurchases) * 100, 2)
        AS PurchaseRate

FROM player_statistics

GROUP BY EngagementLevel

ORDER BY AveragePlaytime DESC;

-- =========================================
-- Mini Analysis 6:
-- High Engagement Players by Genre
-- =========================================

SELECT
    GameGenre,

    COUNT(*) AS TotalPlayers,

    ROUND(AVG(PlayTimeHours), 2)
        AS AveragePlaytime

FROM player_statistics

WHERE EngagementLevel = 'High'

GROUP BY GameGenre

ORDER BY AveragePlaytime DESC;