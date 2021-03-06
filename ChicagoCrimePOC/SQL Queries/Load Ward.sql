/****** Script for SelectTopNRows command from SSMS  ******/
SELECT
	   Ward.WardKey
	  ,Ward.WardCode
	  ,CAST([Latitude_ward] AS DECIMAL(9,6)) AS Latitude
	  ,CAST([Longitude_ward] AS DECIMAL(9,6)) AS Longitude
      ,CAST([sequence_ward] AS INT) AS Sequence
  INTO D_Ward_Polygon
  FROM [geo_dimensions] geo
  JOIN D_Ward ward
	ON geo.ward = ward.wardcode
  WHERE ISNULL(LTRIM(RTRIM(Longitude_ward)),'') <> ''
ORDER BY WardKey, Sequence