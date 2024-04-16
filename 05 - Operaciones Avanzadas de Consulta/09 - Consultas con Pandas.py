# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(user="root", password="root", database="world")

# Recuperar los datos
country_df = pd.read_sql(sql="SELECT * FROM country", con=conn)
city_df = pd.read_sql(sql="SELECT * FROM city", con=conn)
countrylanguage_df = pd.read_sql(sql="SELECT * FROM countrylanguage", con=conn)

# Aplicar INNER JOIN
inner_join_df = pd.merge(left=country_df, right=city_df, how="inner", left_on="Code", right_on="CountryCode")
inner_join_sql = pd.read_sql(sql="SELECT * FROM country INNER JOIN city ON country.Code = city.CountryCode", con=conn)
if inner_join_df.shape == inner_join_sql.shape:
    print("La salida ha sido la misma")
    
# Aplicar LEFT JOIN
left_join_df = pd.merge(left=country_df, right=city_df, how="left", left_on="Code", right_on="CountryCode")
left_join_sql = pd.read_sql(sql="SELECT * FROM country LEFT JOIN city ON country.Code = city.CountryCode", con=conn)
if left_join_df.shape == left_join_sql.shape:
    print("La salida ha sido la misma")
    
# Aplicar RIGHT JOIN
right_join_df = pd.merge(left=country_df, right=city_df, how="right", left_on="Code", right_on="CountryCode")
right_join_sql = pd.read_sql(sql="SELECT * FROM country RIGHT JOIN city ON country.Code = city.CountryCode", con=conn)
if right_join_df.shape == right_join_sql.shape:
    print("La salida ha sido la misma")
    
# Aplicar UNION
union_df = pd.concat([country_df["Name"], city_df["Name"]]).drop_duplicates().to_frame()
union_sql = pd.read_sql(sql="SELECT Name FROM country UNION SELECT Name FROM city", con=conn)
if union_df.shape == union_sql.shape:    
    print("La salida ha sido la misma")

# Aplicar UNION ALL
union_all_df = pd.concat([country_df["Name"], city_df["Name"]], ignore_index=True).to_frame()
union_all_sql = pd.read_sql(sql="SELECT Name FROM country UNION ALL SELECT Name FROM city", con=conn)
if union_all_df.shape == union_all_sql.shape:    
    print("La salida ha sido la misma")
    
# Aplicar BETWEEN
between_df = country_df[country_df["Population"].between(1_000_000, 2_000_000)]
between_sql = pd.read_sql(sql="SELECT * FROM country WHERE Population BETWEEN 1000000 AND 2000000", con=conn)
if between_df.shape == between_sql.shape:
    print("La salida ha sido la misma")

# Aplicar LIKE
like_df = country_df[country_df["Name"].str.contains("land")]
like_sql = pd.read_sql(sql="SELECT * FROM country WHERE Name LIKE '%land%'", con=conn)
if like_df.shape == like_sql.shape:
    print("La salida ha sido la misma")
    
# Aplicar IN
in_df = country_df[country_df["Continent"].isin(["Europe", "Asia"])]
in_sql = pd.read_sql(sql="SELECT * FROM country WHERE Continent IN ('Europe', 'Asia')", con=conn)
if in_df.shape == in_sql.shape:
    print("La salida ha sido la misma")
    
# Aplicar LIMIT
limit_df = country_df.iloc[:10]
limit_sql = pd.read_sql(sql="SELECT * FROM country LIMIT 10", con=conn)
if limit_df.shape == limit_sql.shape:
    print("La salida ha sido la misma")
    
# Recordatorio:
#   - Pandas es una poderosa herramienta que nos permite realizar tratamiento y filtración de información
