WITH tmp AS(
      SELECT DISTINCT *
      FROM `data-to-insights.ecommerce.rev_transactions`
      -- Removing duplicated values
),
tmp1 AS (
  SELECT 
    tmp.channelGrouping,
    tmp.date,
    tmp.geoNetwork_country,
    SUM(tmp.totals_transactions) as tt
  FROM tmp
  GROUP BY 1,2,3
),
tmp2 AS (
  SELECT 
    channelGrouping,
    ARRAY_AGG(STRUCT(geoNetwork_country, PARSE_DATE("%Y%m%d", date) AS date)) AS repeatedcols,
    ARRAY_AGG( tmp1.tt ) AS TotalTransaction
  FROM tmp1
  GROUP BY 1
)

SELECT 
  channelGrouping,
  ARRAY(SELECT AS STRUCT 
     geoNetwork_country AS Country,
     ARRAY_AGG(DISTINCT date ORDER BY date) AS date
   FROM UNNEST(repeatedcols)
   GROUP BY 1
   ) AS agg,
   tmp2.TotalTransaction
FROM tmp2