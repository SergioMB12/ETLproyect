<a href="https://www.gifsanimados.org/cat-alcohol-328.htm"><img src="https://www.gifsanimados.org/data/media/328/alcohol-imagen-animada-0116.gif" border="0" alt="alcohol-imagen-animada-0116" /></a>

# ETL proyect

## Motivación del proyecto

-Tomando como punto de partida un csv de kaggel.Y con el uso de tecnicas de scraping, y enriquecimiento de datos.Hemos obtenido un data frame de calidad e información suficiente para analizar diversos aspectos relativos a la salud y habitos de los habitantes de distintos paises.

## 1- Obtención de los datos y limpieza de datos:

-Los datos sobre ataques son descargados de la web [Kaggle](https://www.kaggle.com/sansuthi/alcohol-consumption).En concreto nos descargamos el csv que usaremos de punto de partida.

-Posteriormente obtenemos dos csv más el primero de [kaggle](https://www.kaggle.com/majyhain/death-cause-by-country) nuevamente y el otro de la siguiente [web](https://worldpopulationreview.com/country-rankings/smoking-rates-by-country).

-Despues y como se puede observar en los archivos de scraping de este repositorio.Obtenemos más información para enriquecer nuestro data frame.Dichos datos salen de [ la web ](https://www.worlddata.info/life-expectancy.php) y de [wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate)

## 2- Creación de base de datos SQL

Todos los datos obtenidos tras este proceso de scraping y enriquecimiento son almacenados en una base de datos creada en sql con el nombre de countries_db.

## 3- To do:

-Continuar ampliando la base de datos sql incorporando más datos de calidad y con relación a los ya existentes.

-Generar graficas y visualizaciones de datos para dar respuesta a las posibles hipotesis que surgan en relación a los datos obtenidos.

## Tecnología usada


[python](https://docs.python.org/3/)

[pandas](https://pandas.pydata.org/)

[numpy](https://numpy.org/)

[regex](https://docs.microsoft.com/es-es/dotnet/api/system.text.regularexpressions.regex?view=net-6.0)

[selenium](https://www.selenium.dev/)

[beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[sql](https://www.mysql.com/)








