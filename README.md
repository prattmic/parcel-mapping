# Chatham County Parcel Google Maps visualization

# Steps

1. Download `Parcels_withtax` from
   ftp://ftp.chathamnc.org/TaxMapping%28Parcels%29/ and extract.

2. Import the .shp file as a vector layer into QGIS.

3. Zoom to region of interest.

4. Export vector layer as KML to parcel.kml. Limit the "Extent" to the "Map
   View".

5. If the KML is bigger than 5MB, run `split.py` to split the KML into many
   smaller KMLs.

5. Import into Google My Maps.

Note: The more data that is imported into Google Maps, the worse it performs.
