# Name : WebMapFolium
# About : Web Map created with the folium library
# Created by : Chantel Williams
# Date : February 2024

import constants as cn
import folium
import geopandas
import os


def create_map():
    # https://leaflet-extras.github.io/leaflet-providers/preview/
    m = folium.Map(location=(35.713118, -76.3797879),
                   control_scale=True,
                   zoom_start=11,
                   min_lat=35.7085,
                   max_lat=35.7432,
                   min_lon=-76.3473,
                   max_lon=-76.3631)

    m.save(r"C:\PersonalProject\web-projects\test-site\Pocosin_FWS.html")
    return m


class Map_Site:
    def __init__(self,
                 site_extent=cn.site_extent,
                 ):
        self.site_extent = site_extent
        self.map_object = create_map()

    def initialize_map_site(self):
        self.add_site_data_to_map()
        self.save_map()
        return

    def execute_map_site(self):
        self.initialize_map_site()

    def add_feature_to_map(self, site_data, site_name):
        geopandas_object = geopandas.read_file(site_data)
        geopandas_object_reprojected = geopandas_object.to_crs(epsg=4326)
        # folium.GeoJson(data=aoi_geopandas, name=f'{aoi_geopandas["DIVNAME"][0]}').add_to(m)
        folium.GeoJson(data=geopandas_object_reprojected['geometry'][0], name=f'{geopandas_object_reprojected[f"{site_name}"][0]}').add_to(self.map_object)
        # self.map_object.save(r"C:\PersonalProject\web-projects\test-site\Pocosin_FWS.html")
        return

    def add_site_data_to_map(self):
        self.add_feature_to_map(self.site_extent, "DIVNAME")  # site_extent
        return

    def save_map(self):
        folium.LayerControl().add_to(self.map_object)
        self.map_object.save(r"C:\PersonalProject\web-projects\test-site\Pocosin_FWS.html")
        return

def main():
    MS = Map_Site()
    MS.execute_map_site()


if __name__ == "__main__":
    main()
