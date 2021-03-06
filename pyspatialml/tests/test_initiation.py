from unittest import TestCase
from pyspatialml import Raster, RasterLayer
import rasterio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
test_dir = os.path.dirname(__file__)
pkg_dir = os.path.join(test_dir, os.path.pardir)
nc_dir = os.path.join(pkg_dir, 'nc_dataset')

class TestInit(TestCase):

    band1 = os.path.join(nc_dir, 'lsat7_2000_10.tif')
    band2 = os.path.join(nc_dir, 'lsat7_2000_20.tif')
    band3 = os.path.join(nc_dir, 'lsat7_2000_30.tif')
    band4 = os.path.join(nc_dir, 'lsat7_2000_40.tif')
    band5 = os.path.join(nc_dir, 'lsat7_2000_50.tif')
    band7 = os.path.join(nc_dir, 'lsat7_2000_70.tif')
    predictors = [band1, band2, band3, band4, band5, band7]

    def test_initiation(self):

        # file paths ----------------------
        # test init from list of file paths
        stack = Raster(self.predictors)
        self.assertIsInstance(stack, Raster)
        self.assertEqual(stack.count, 6)
        stack = None

        # test init from single file path
        stack = Raster(self.band1)
        self.assertIsInstance(stack, Raster)
        self.assertEqual(stack.count, 1)
        stack = None

        # rasterio.io.datasetreader --------
        # test init from single rasterio.io.datasetreader
        with rasterio.open(self.band1) as src:
            stack = Raster(src)
            self.assertIsInstance(stack, Raster)
            self.assertEqual(stack.count, 1)
            stack = None

        # test init from list of rasterio.io.datasetreader objects
        srcs = []
        for f in self.predictors:
            srcs.append(rasterio.open(f))
        stack = Raster(srcs)
        self.assertIsInstance(stack, Raster)
        self.assertEqual(stack.count, 6)
        stack = None

        # rasterio.band ---------------------
        # test init from single rasterio.band object
        with rasterio.open(self.band1) as src:
            band = rasterio.band(src, 1)
            stack = Raster(band)
            self.assertIsInstance(stack, Raster)
            self.assertEqual(stack.count, 1)
            stack = None

        # test init from list of rasterio.band objects
        bands = []
        for f in self.predictors:
            src = rasterio.open(f)
            bands.append(rasterio.band(src, 1))
        stack = Raster(bands)
        self.assertIsInstance(stack, Raster)
        self.assertEqual(stack.count, 6)
        stack = None

        # RasterLayer objects ---------------
        # test init from a single RasterLayer object
        with rasterio.open(self.band1) as src:
            band = rasterio.band(src, 1)
            layer = RasterLayer(band)
            stack = Raster(layer)
            self.assertIsInstance(stack, Raster)
            self.assertEqual(stack.count, 1)
            stack = None

        # test init from a list of RasterLayer objects
        layers = []
        for f in self.predictors:
            src = rasterio.open(f)
            band = rasterio.band(src, 1)
            layers.append(RasterLayer(band))
        stack = Raster(layers)
        self.assertIsInstance(stack, Raster)
        self.assertEqual(stack.count, 6)
        stack = None
