Analytical queries:

Analytical query for Sum of Acres based on LandUseCode

SELECT 
	id, 
        LandUse1,
	Acres, 
	Shape_STAr, 
	Shape_STLe,
    SUM(Acres) as SUM_ACRES
FROM test.parcels_public GROUP BY LandUse1;



Query for finding parcels after given parcel using Lead analytic function. Useful if we want to know what parcels surrounds given parcel  


SELECT 
	id, 
        LandUse1,
	Acres, 
	Shape_STAr, 
	Shape_STLe,
    LEAD(LandUse1, 1) OVER(ORDER BY Acres) AS FirstOffset,
    LEAD(LandUse1, 2) OVER(ORDER BY Acres) AS SecondOffset
FROM test.parcels_public;


Query to find parcel before given parcel

SELECT 
	id, 
        LandUse1,
	Acres, 
	Shape_STAr, 
	Shape_STLe,
    LAG(LandUse1, 1) OVER(ORDER BY Acres) AS FirstOffset,
    LAG(LandUse1, 2) OVER(ORDER BY Acres) AS SecondOffset
FROM test.parcels_public;




SELECT 
	id, 
	Acres, 
	Shape_STAr, 
	Shape_STLe,
	CUME_DIST() OVER(ORDER BY Acres) AS CDF_Acres
FROM test.parcels_public;



SELECT 
	id, 
        LandUse1,
	Acres, 
	Shape_STAr, 
	Shape_STLe,
    FIRST_VALUE(LandUse1) OVER(ORDER BY Acres) AS FirstValue
FROM test.parcels_public;


