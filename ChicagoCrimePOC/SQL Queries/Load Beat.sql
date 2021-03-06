DROP TABLE D_Beat_Polygon

SELECT
	   BEAT.BeatKey
	  ,BEAT.BeatCode_Full
	  ,BEAT.BeatName
	  ,CAST([Latitude_beat] AS DECIMAL(9,6)) AS Latitude
	  ,CAST([Longitude_beat] AS DECIMAL(9,6)) AS Longitude
      ,CAST([sequence_beat_ed] AS INT) AS Sequence
  INTO D_Beat_Polygon
  FROM [geo_dimensions] geo
  JOIN D_Beat BEAT
	ON geo.BEAT_NUM = BEAT.BeatCode_Full
  WHERE ISNULL(LTRIM(RTRIM(Longitude_beat)),'') <> ''
ORDER BY BEAT.BeatKey, Sequence