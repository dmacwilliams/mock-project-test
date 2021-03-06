/****** Script for SelectTopNRows command from SSMS  ******/
DROP TABLE D_PoliceDistrict_Polygon

SELECT
	   PD.PoliceDistrictKey
	  ,PD.PoliceDistrictCode
	  ,PD.PoliceDistrictName
	  ,CAST([Latitude_district] AS DECIMAL(9,6)) AS Latitude
	  ,CAST([Longitude_district] AS DECIMAL(9,6)) AS Longitude
      ,CAST([sequence_district] AS INT) AS Sequence
  INTO D_PoliceDistrict_Polygon
  FROM [geo_dimensions] geo
  JOIN D_PoliceDistrict PD
	ON geo.dist_num = CAST(PD.policedistrictcode AS INT)
  WHERE ISNULL(LTRIM(RTRIM(Longitude_district)),'') <> ''
ORDER BY PD.PoliceDistrictKey, Sequence