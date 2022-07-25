import pymysql

"""
Create two SQL tables to add the data. I am using AWS RDS database for this

"""

def create_SQL_table(host, dbUserName, dbUserPassword, cusrsorType):
    conn   = pymysql.connect(host=host,
                         user=dbUserName,
                         password=dbUserPassword,
                         cursorclass=cusrsorType)

    dbCursor = conn.cursor()                              
    # SQL query string
    sqlQuery = """
               CREATE TABLE test.`Land_Use_Code_Report_v3` (
                                  `Land_Use_Code` VARCHAR(10),
                                  `Descr` text,
                                  `Direct_Chrg_Class` text,
                                  `Dwelling_Type` double DEFAULT NULL,
                                  `Use_Category` text,
                                  `BOECategory` int DEFAULT NULL,
                                  `Is_Apply_Inflation` text,
                                  `Status` text,
                                  `DTS` text,
                                   PRIMARY KEY (Land_Use_Code)
                              );
               """

    # Execute the sqlQuery
    dbCursor.execute(sqlQuery)
    
    # Create second table ""

    SQLQuery2 = """
              CREATE TABLE test.`parcels_public_v2` (
                                `id` int NOT NULL,
                                `ASMT` text,
                                `ASMTWithDa` text,
                                `Acres` double DEFAULT NULL,
                                `LandUse1` VARCHAR(10),
                                `TRA` text,
                                `floor` int DEFAULT NULL,
                                `Notes` text,
                                `Shape_STAr` double DEFAULT NULL,
                                `Shape_STLe` double DEFAULT NULL,
                                `geometry` text,
                                 PRIMARY KEY (`id`),
                                 FOREIGN KEY (`LandUse1`) REFERENCES test.`Land_Use_Code_Report`(Land_Use_Code)
                   );
               """

    dbCursor.execute(SQLQuery2)

    #Fetch all the rows
    databaseCollection = dbCursor.fetchall()

    for datatbase in databaseCollection:
       print(datatbase)


    conn.close()

