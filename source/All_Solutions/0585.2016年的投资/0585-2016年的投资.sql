SELECT SUM(insurance.TIV_2016) AS TIV_2016
FROM
insurance
where insurance.TIV_2015 IN
    #2015��Ͷ�ʲ�Ψһ��ά��Ψһ
	(SELECT TIV_2015 FROM insurance t GROUP BY TIV_2015 HAVING COUNT(*)>1)
	AND
	CONCAT(LAT,CONCAT(',',LON)) IN(
	SELECT CONCAT(LAT,CONCAT(',',LON))
	FROM insurance
	GROUP BY LAT,LON
	HAVING COUNT(*)=1
	)