SELECT
        ROUND(AVG(LAT_N),4) AS median
FROM (
        SELECT
                LAT_N,
                ROW_NUMBER() OVER(ORDER BY LAT_N) AS row_num,
                COUNT(LAT_N) OVER() AS total_rows
        FROM STATION) AS numbered
WHERE 
        row_num IN (FLOOR((total_rows+1)/2.0), CEIL((total_rows+1)/2.0));