# -*- coding: utf-8 -*-
"""SpaceX_FoliumMap_week3ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kOsA66RVGi823GiIenZXp_d05QaUnb-3

#Launch Site Exploration with Folium
In the realm of space exploration, launch success hinges on a multitude of factors, including the weight of the payload, the targeted orbit, and even the launch site itself. The initial trajectory of a rocket, dictated by its launch location and surrounding environment, could potentially influence its success.  Therefore, selecting an optimal site for future launches requires a comprehensive analysis, and this lab aims to leverage data visualization to uncover potential geographical trends influencing launch outcomes.

Building upon your prior exploration of the SpaceX launch dataset using Matplotlib and Seaborn, this lab delves into the realm of interactive visual analytics with Folium. Here, we embark on a journey to achieve the following objectives:

Task 1: Mapping the Launch Sites: We will pinpoint all launch locations on an interactive map.
Task 2: Visualizing Launch Success/Failure: We will differentiate between successful and failed launches for each site using distinct markers on the map.
Task 3: Unveiling Geographical Relationships: We will calculate distances between launch sites and their surrounding features, aiming to discover potential geographical patterns that might influence launch success rates.
By completing these tasks, we hope to gain valuable insights into the geographical considerations when selecting future launch sites.

Now, let's proceed by importing the necessary Python libraries to embark on this exploration!
"""

!pip install folium

"""Delving into the World of Interactive Maps with Folium in Python
In the realm of Python programming, the Folium library emerges as a powerful tool for crafting captivating and informative interactive web maps. Built upon the foundation of Leaflet, an open-source JavaScript library for map rendering, Folium empowers you to generate dynamic and insightful maps without the intricacies of JavaScript programming.

Key Features of Folium:

Base Map Selection: Folium presents a diverse range of base maps to choose from, including OpenStreetMap, Stamen, and Thunderforest, catering to your specific mapping needs.

Marker Placement: Effortlessly add custom markers to your map, specifying their location, color, and iconic symbols to effectively represent your data points.

Spatial Data Visualization: Seamlessly visualize your spatial data, encompassing points, lines, and polygons, directly onto the map, bringing your data to life.

Interactive Popups: Enhance your map with informative popups, displaying relevant details associated with each marker or spatial element upon user interaction.

Map Events: Respond to user actions such as clicks, mouse movements, and zoom events, making your maps truly interactive and engaging.

Map Controls: Empower your users with intuitive map controls, enabling them to zoom, pan, and navigate the map with ease.

HTML Output: Generate your maps as HTML files, ready to be shared or embedded within your web applications.

Benefits of Utilizing Folium:

Effortless Learning: Folium boasts an intuitive user interface and comprehensive documentation, making it easy to learn and adopt.

Interactive Nature: Folium maps are interactive, allowing users to explore and grasp data insights visually.

Customization Flexibility: Folium offers a wide spectrum of customization options, enabling you to tailor your maps to your specific needs.

Web-Based Accessibility: Folium maps function seamlessly on web browsers, eliminating the need for additional software installations.

Applications of Folium:

Spatial Analysis: Visualize and explore spatial data to identify patterns, trends, and relationships within geographical contexts.

Data Presentation: Share spatial insights with a broader audience in an engaging and visually appealing manner.

Web Application Development: Integrate interactive maps into web applications to enhance user experience and provide data-driven insights.

Educational Purposes: Facilitate the understanding of geographical concepts and spatial data among students.
"""

import folium  #"The goal of the project is to showcase the flexibility of using different libraries for different tasks."
import pandas as pd

# Import folium MarkerCluster plugin
from folium.plugins import MarkerCluster
# Import folium MousePosition plugin
from folium.plugins import MousePosition
# Import folium DivIcon plugin
from folium.features import DivIcon

"""If you need to refresh your memory about folium, you may download and refer to this previous folium lab:

# Task 1: Mark all launch sites on a map
First, let's try to add each site's location on a map using site's latitude and longitude coordinates

The following dataset with the name spacex_launch_geo.csv is an augmented dataset with latitude and longitude added for each site.
"""

!pip install js
!pip install fetch

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv'

df = pd.read_csv(URL)

df.head()

df.info()

df.describe()

#Explanation:
#"We extract" is a common phrase used to describe the process of retrieving specific information from a dataset or data source.
#"Launch site" refers to the location from which a rocket or spacecraft is launched.
#"Latitude" and "longitude" are geographical coordinates that specify the location of a point on Earth's surface.
#"Success class" indicates whether a particular launch was successful or not.
spacex_df = df[['Launch Site', 'Lat', 'Long', 'class']]
spacex_df

#"Group the dataframe by the 'launch site' column using the groupby method."
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
launch_sites_df

"""Above coordinates are just plain numbers that can not give you any intuitive insights about where are those launch sites. If you are very good at geography, you can interpret those numbers directly in your mind. If not, that's fine too. Let's visualize those locations by pinning them on a map.

We first need to create a folium Map object, with an initial center location to be NASA Johnson Space Center at Houston, Texas.
"""

#We have the coordinates. The latitude and longitude have been provided to us.
# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]

site_map = folium.Map(location=nasa_coordinate, zoom_start=10)  #The provided code currently generates a blank map.

#circle_method
#The provided code snippet demonstrates how to create a circle on a map with a red border. It utilizes the folium library in Python.
# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
#This line stores the coordinates of the NASA Johnson Space Center in a list. The latitude and longitude coordinates are stored in the first and second elements of the list, respectively.
circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
#folium.Circle is a function to create a circle on the map.
#nasa_coordinate specifies the coordinates of the circle's center.
#radius sets the circle's radius in meters.
#color defines the color of the circle's border.
#fill determines whether the circle should be filled or not.
#folium.Popup is a function to create a popup on the map.
#'NASA Johnson Space Center' specifies the title of the popu
# Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
#This line creates a circle with the center at nasa_coordinate, a radius of 1000 meters, and a red border color (#d35400). Additionally, the circle is filled with a popup titled "NASA Johnson Space Center
marker = folium.map.Marker(                       #This line creates a marker at the nasa_coordinate with a custom icon. The icon includes a text label with the title "NASA Johnson Space Center".
    nasa_coordinate,
    # Create an icon as a text label   folium.map.Marker is a function to create a marker on the map.
    #nasa_coordinate specifies the coordinates of the marker.
    #icon defines a folium.Icon object that defines the marker's appearance.
    #icon_size sets the icon's size in pixels.
    #icon_anchor specifies the anchor position of the icon.
    #html defines the HTML code for the icon's content.
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)  #This line adds the circle to the map.
site_map.add_child(marker)  #This line adds the marker to the map.

#The Folium library loads the Leaflet JavaScript library to create the interactive map.
#The Map function creates a new Map object that displays the map.
#The coordinates of nasa_coordinate are set as the center of the map.
#The zoom level of the map is set to 5.
#The Map object is assigned to the variable site_map.
#The variable site_map now contains an interactive map that is centered on the coordinates nasa_coordinate with a zoom level of 5.
site_map = folium.Map(location=nasa_coordinate, zoom_start=5)

launch_sites_df
#CCAFS LC-40: This launch site is located at coordinates (28.562302, -80.577356).
#CCAFS SLC-40: This launch site is located at coordinates (28.563197, -80.576820).
#KSC LC-39A: This launch site is located at coordinates (28.573255, -80.646895).

CCAFSLC_coordinate = [28.562302, -80.577356]
#atitude and longitude coordinates, specifically 28.562302 degrees latitude and -80.577356 degrees longitude.
site_mapLC = folium.Map(location=CCAFSLC_coordinate, zoom_start=10)
#It uses the folium.Map function from the folium library.
#In summary, this code snippet creates a basic map centered around the specified coordinates (likely Cape Canaveral Air Force Station Launch Complex) with a zoom level of 10 using the folium library.

# Create a blue circle at launch site coordinate with a popup label showing its name
#CCAFSLC_coordinate: This variable (not shown in the code snippet) presumably holds the latitude and longitude coordinates of the launch site (likely Cape Canaveral Air Force Station Complex - CCAFS SLC).
#radius=1000: This sets the radius of the circle in meters (here, 1000 meters).
#color='#d35400': This defines the color of the circle using a hex code (#d35400 represents orange-red). You can change this to any desired color code (e.g., '#0000FF' for blue).
#fill=True: This fills the circle with the specified color.
#.add_child(folium.Popup('launch site Space Center')): This line adds a popup element to the circle. When you click on the circle on the map, a small box will appear with the text "launch site Space Center" (text can be modified
circle = folium.Circle(CCAFSLC_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('launch site Space Center'))
# Create a blue circle at launch site Space Center coordinate with a icon showing its name
marker = folium.map.Marker(
    CCAFSLC_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSLC',
        )
    )
#icon=DivIcon(...): This defines a custom icon for the marker using DivIcon.
#icon_size=(20,20): Sets the size of the icon in pixels (here, 20x20 pixels).
#icon_anchor=(0,0): Defines the anchor point of the icon. This sets the location where the marker points to within the icon itself (here, top-left corner).
#html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSLC': This part creates the HTML content for the custom icon.
#The <div> element defines a styled box.
#style="font-size: 12; color:#d35400;": Sets the font size (12px) and color (orange-red) for the text within the icon.
#<b>%s</b>: This is a placeholder for text. The %s gets replaced with the string 'CCAFSLC' during code execution, resulting in "CCAFSLC" displayed in bold within the icon.
site_map.add_child(circle)
site_map.add_child(marker)

circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
marker = folium.map.Marker(                       #This line creates a marker at the nasa_coordinate with a custom icon. The icon includes a text label with the title "NASA Johnson Space Center".
    nasa_coordinate,
                                                      icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)  #This line adds the circle to the map.
site_map.add_child(marker)  #This line adds the marker to the map.

circle = folium.Circle(CCAFSLC_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('launch site Space Center'))
marker = folium.map.Marker(
    CCAFSLC_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSLC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)

"""# Task 2: Mark the success/failed launches for each site on the map
Next, let's try to enhance the map by adding the launch outcomes for each site, and see which sites have high success rates. Recall that data frame spacex_df has detailed launch records, and the class column indicates if this launch was successful or not
"""

launch_sites_df
#a map visualization showing launch locations and their success/failure outcomes

nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)
#---------------------------------------
CCAFSLC_coordinate = [28.562302, -80.577356]
site_mapLC = folium.Map(location=CCAFSLC_coordinate, zoom_start=10)
#------------------------------------------
CCAFSSLC_coordinate = [28.563197, -80.576820]
site_mapLC = folium.Map(location=CCAFSSLC_coordinate, zoom_start=10)
#--------------------------------------------
KSCLC_coordinate = [28.573255, -80.646895]
site_mapLC = folium.Map(location=KSCLC_coordinate, zoom_start=10)
#-----------------------------------------
VAFBSLC_coordinate = [34.632834, -120.610746]
site_mapLC = folium.Map(location=VAFBSLC_coordinate, zoom_start=10)
#The following lines (commented out with #---) create separate map objects (site_mapLC) for four other locations: CCAFSLC, CCAFSSLC, KSCLC, and VAFBSLC.
#Each line defines a map centered on the specific coordinates for each launch site with a starting zoom level of 10.
#However, the variable name site_mapLC is reused for each map, which would overwrite the previous map object.
#Overall:
#The code creates a map for NASA Headquarters and seems to intend to create separate maps for four launch sites (CCAFSLC, CCAFSSLC, KSCLC, and VAFBSLC). However, it does this inefficiently by reusing the same variable name (site_mapLC) for each map, resulting in only the last map being stored.

# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
#The code seems to be using the folium library for creating interactive web maps.
#It assumes variables like nasa_coordinate, CCAFSLC_coordinate, CCAFSSLC_coordinate, KSCLC_coordinate, and VAFBSLC_coordinate are defined elsewhere, likely containing geographic coordinates for each location.
#A variable named site_map is assumed to be a map object already created using folium.
#circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
# Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)
#--------------------------------------------------
# Create a blue circle at launch site coordinate with a popup label showing its name
circle = folium.Circle(CCAFSLC_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('CCAFSLC Space Center'))
# Create a blue circle at launch site Space Center coordinate with a icon showing its name
marker = folium.map.Marker(
    CCAFSLC_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSLC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)
#-------------------------------------------
# Create a blue circle at launch site coordinate with a popup label showing its name
circle = folium.Circle(CCAFSSLC_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('CCAFSSLC Space Center'))
# Create a blue circle at launch site Space Center coordinate with a icon showing its name
marker = folium.map.Marker(
    CCAFSSLC_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSSLC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)
#-----------------------------------------------
# Create a blue circle at launch site coordinate with a popup label showing its name
circle = folium.Circle(KSCLC_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('KSCLC Space Center'))
# Create a blue circle at launch site Space Center coordinate with a icon showing its name
marker = folium.map.Marker(
    KSCLC_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'KSCLC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)
#------------------------------------------------
# Create a blue circle at launch site coordinate with a popup label showing its name
circle = folium.Circle(VAFBSLC_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('VAFBSLC Space Center'))
# Create a blue circle at launch site Space Center coordinate with a icon showing its name
marker = folium.map.Marker(
    VAFBSLC_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'VAFBSLC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)

spacex_df.tail(10)

"""To visualize the launch history, we'll place markers on a map for each launch. Successful launches (class 1) will be marked in green, while failed attempts (class 0) will be red. It's important to note that launches typically occur from a limited number of sites, so expect to see markers clustered together. To avoid overwhelming the map, we'll use a special technique called Marker Clustering to group these overlapping markers."""

marker_cluster = MarkerCluster()

# Function to assign color to launch outcome.
# We created a function called assign_marker_color that returns 'green' if launch_outcome is equal to 1 and 'red' otherwise.
def assign_marker_color(launch_outcome):
    if launch_outcome == 1:
        return 'green'
    else:
        return 'red'
#"Apply the function row by row. Iterate through each row and apply the function. Then, once you understand all rows, take the result and display it in the marker_color column."
spacex_df['marker_color'] = spacex_df['class'].apply(assign_marker_color)
spacex_df.tail(10)

#Finally, we'll write a loop that iterates over each row of our dataframe and retrieves the latitude, longitude, and color for each row. It then adds this information to the initial marker cluster.
# Add marker_cluster to current site_map
site_map.add_child(marker_cluster)

# for each row in spacex_df data frame
# create a Marker object with its coordinate
# and customize the Marker's icon property to indicate if this launch was successed or failed,
# e.g., icon=folium.Icon(color='white', icon_color=row['marker_color']
for index, row in spacex_df.iterrows():
    # create and add a Marker cluster to the site map
    coordinate = [row['Lat'], row['Long']]
    folium.map.Marker(coordinate, icon=folium.Icon(color='white',icon_color=row['marker_color'])).add_to(marker_cluster)
site_map

"""# TASK 3: Calculate the distances between a launch site to its proximities

Next, we need to explore and analyze the proximities of launch sites.

Let's first add a MousePosition on the map to get coordinate for a mouse over a point on the map. As such, while you are exploring the map, you can easily find the coordinates of any points of interests (such as railway)
"""

# Add Mouse Position to get the coordinate (Lat, Long) for a mouse over on the map
formatter = "function(num) {return L.Util.formatNum(num, 5);};"  #The line formatter = "function(num) {return L.Util.formatNum(num, 5);};" (if included) defines a custom function named formatter that takes a number (num) as input and returns it formatted with five decimal places using the L.Util.formatNum function (assumed to be from the Leaflet library). This is likely used for displaying latitude and longitude coordinates with a specific level of precision.
mouse_position = MousePosition(  #The line mouse_position = MousePosition(...) creates a MousePosition control object, which is a user interface element typically displayed as a small box that shows the current mouse cursor position on the map. The arguments passed to the MousePosition constructor configure its behavior:
    position='topright',  #position='topright': This sets the position of the control to the top-right corner of the map.
    separator=' Long: ',  #separator=' Long: ': This defines the separator string inserted between latitude and longitude values (' Long: ').
    empty_string='NaN',   #empty_string='NaN': This specifies the string to display when no coordinates are available ('NaN').
    lng_first=False,      #lng_first=False: This indicates that latitude should be displayed before longitude (default is True).
    num_digits=20,        #num_digits=20: This sets the maximum number of digits to display for coordinates (default is likely lower).
    prefix='Lat:',        #prefix='Lat:': This defines the prefix string to show before latitude ('Lat:').
    lat_formatter=formatter,  #lat_formatter=formatter: This assigns the custom formatter function (if defined) to format latitude values.
    lng_formatter=formatter,  #lng_formatter=formatter: This assigns the custom formatter function (if defined) to format longitude values.
)

site_map.add_child(mouse_position)
site_map
#Overall Functionality:
#When this code is executed, a mouse position control will appear in the top-right corner of the map. As you move the mouse over the map, the control will dynamically update to show the current latitude and longitude coordinates, formatted with the specified options (e.g., five decimal places, separator string, prefix).
#Additional Considerations:
#The code assumes the use of the Leaflet JavaScript library for interactive maps.
#The purpose of L.Util.formatNum depends on the specific implementation in Leaflet.

#Calculating the distance between two points using mouse position(To calculate the distance between two points using the mouse position, you can utilize the Pythagorean theorem)
from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0
#This function takes four points from us.The latitude and longitude of point 1 and the latitude and longitude of point 2.We want to calculate the distance between point one and point two.
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
 #Pythagorean theorem
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# We define the latitude and longitude of points one and two.
# find coordinate of the closet coastline
# e.g.,: Lat: 28.56367  Lon: -80.57163
# distance_coastline = calculate_distance(launch_site_lat, launch_site_lon, coastline_lat, coastline_lon)
launch_site_lat = 28.563197
launch_site_lon = -80.576820
coastline_lat = 28.56334
coastline_lon = -80.56799
# Then we call the function.
distance_coastline = calculate_distance(launch_site_lat, launch_site_lon, coastline_lat, coastline_lon)
print(distance_coastline,' km')

#To draw a point on a map using the folium.marker method.The provided code snippet defines a marker on a map using the folium.Marker method and customizes its appearance with DivIcon.
distance_marker = folium.Marker(  #his line creates a marker object named distance_marker using the folium.Marker function.
    coordinate,  #This argument likely represents the latitude and longitude coordinates of the point you want to mark on the map. It's assumed you have this variable defined elsewhere in your code.
    icon=DivIcon(  # This sets a custom icon for the marker using the DivIcon class. DivIcon allows you to define the icon as HTML content instead of an image.
        icon_size=(20,20),  # This defines the size of the icon as a width of 20 pixels and a height of 20 pixels.
        icon_anchor=(0,0),  # This sets the anchor point of the icon. By default, the anchor point is at the center of the icon. Setting it to (0,0) places it at the top-left corner.
        #Save the map as an HTML file
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance_coastline),
        )  #This defines the HTML content that will be displayed as the icon.
    )
#The HTML code creates a <div> element with specific styles:
#font-size: 12: Sets the font size to 12 pixels.
#color:#d35400: Sets the text color to orange (#d35400).
#<b>%s</b>: This is a placeholder that will be replaced with another string value.
#The "{:10.2f} KM".format(distance_coastline) part formats a floating-point number representing the distance (presumably in kilometers) and appends " KM" to it. The {:10.2f} ensures the number is displayed with two decimal places and a total width of 10 characters. The .format(distance_coastline) replaces %s in the HTML with the formatted distance value.

print(distance_marker)

# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
lines=folium.PolyLine([[28.563197,-80.576820],[28.56341,-80.56806]], weight=1 , color='green') #Starts from the coordinates [28.563197,-80.576820], which seems to be the launch site of your site.Ends at the coordinates [28.56341,-80.56806], which is probably a point on your coastline.
#Is drawn in green color and with a thickness of 1.
coordinates = [[launch_site_lat,launch_site_lon],[coastline_lat,coastline_lon]]
#Takes coordinates from a list named coordinates.
#This list should contain two sublists, each representing the geographic coordinates of a point as [latitude, longitude].
#It seems like this line draws a straight path between your launch site and your coastline.
#Is drawn with a thickness of 1.
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
#In the provided code, the variable names launch_site_lat and launch_site_lon as well as coastline_lat and coastline_lon are used. It seems like these variables should store the latitude and longitude values of your launch site and coastline.
#For this code to work correctly, you need to assign the correct values to these variables.

# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
coordinates = [[launch_site_lat,launch_site_lon],[coastline_lat,coastline_lon]]
lines=folium.PolyLine(locations=coordinates, weight=1)
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)

closest_highway = 28.56335, -80.57085
closest_railroad = 28.57206, -80.58525
closest_city = 28.10473, -80.64531

#We have the latitude and longitude of different places and we measure the distances.
#And with folium.marker and polyline we can draw and have all three of them on the map

distance_highway = calculate_distance(launch_site_lat, launch_site_lon, closest_highway[0], closest_highway[1])
print('distance_highway =',distance_highway, ' km')
distance_railroad = calculate_distance(launch_site_lat, launch_site_lon, closest_railroad[0], closest_railroad[1])
print('distance_railroad =',distance_railroad, ' km')
distance_city = calculate_distance(launch_site_lat, launch_site_lon, closest_city[0], closest_city[1])
print('distance_city =',distance_city, ' km')

# closest highway marker
distance_marker = folium.Marker(
   closest_highway,
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='%s' % "{:10.2f} KM".format(distance_highway),))
site_map.add_child(distance_marker)
# closest highway line
coordinates = [[launch_site_lat,launch_site_lon],closest_highway]
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)

# closest railroad marker
distance_marker = folium.Marker(
   closest_railroad,
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='%s' % "{:10.2f} KM".format(distance_railroad),))
site_map.add_child(distance_marker)
# closest railroad line
coordinates = [[launch_site_lat,launch_site_lon],closest_railroad]
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
# closest city marker
distance_marker = folium.Marker(
   closest_city,
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='%s' % "{:10.2f} KM".format(distance_city),))
site_map.add_child(distance_marker)
# closest city line
coordinates = [[launch_site_lat,launch_site_lon],closest_city]
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)

"""#My Findings
As mentioned before, launch sites are in close proximity to equator to minimize fuel consumption by using Earth's ~ 30km/sec eastward spin to help spaceships get into orbit.
Launch sites are in close proximity to coastline so they can fly over the ocean during launch, for at least two safety reasons-- (1) crew has option to abort launch and attempt water landing (2) minimize people and property at risk from falling debris.
Launch sites are in close proximity to highways, which allows for easily transport required people and property.
Launch sites are in close proximity to railways, which allows transport for heavy cargo.
Launch sites are not in close proximity to cities, which minimizes danger to population dense areas.
Now you have discovered many interesting insights related to the launch sites' location using folium, in a very interactive way. Next, you will need to build a dashboard using Ploty Dash on detailed launch records.
"""