#!/usr/bin/env python

##Copyright 2016 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

import os
import random
import struct

#from OCC.Core.Graphic3d import Graphic3d_ArrayOfPoints
from OCC.Graphic3d import Graphic3d_ArrayOfPoints
#from OCC.Core.AIS import AIS_PointCloud
from OCC.AIS import AIS_PointCloud

from OCC.gp import gp_Pnt
from OCC.Quantity import Quantity_Color, Quantity_TOC_RGB

from OCC.Display.SimpleGui import init_display
display, start_display, add_menu, add_function_to_menu = init_display()


def random_points(event=None):
    n_points = 500000
    # first, create a set of 1000 points
    points_3d = Graphic3d_ArrayOfPoints(n_points)
    for idx in range(n_points):
        x = random.uniform(-50, 50)
        y = random.uniform(-50, 50)
        z = random.uniform(-50, 50)
        points_3d.AddVertex(x, y, z)

    # then build the point cloud
    point_cloud = AIS_PointCloud()
    point_cloud.SetPoints(points_3d.GetHandle())

    # display
    ais_context = display.GetContext().GetObject()
    ais_context.Display(point_cloud.GetHandle())
    display.View_Iso()
    display.FitAll()

def bunny(event=None):
    pcd_file = open(os.path.join('assets', 'models', 'bunny.pcd'), 'r').readlines()[10:]
    # create the point_cloud
    pc = Graphic3d_ArrayOfPoints(len(pcd_file))
    for line in pcd_file:
        x, y, z = map(float, line.split())
        pc.AddVertex(x, y, z)
    point_cloud = AIS_PointCloud()
    point_cloud.SetPoints(pc.GetHandle())
    ais_context = display.GetContext().GetObject()
    ais_context.Display(point_cloud.GetHandle())
    display.View_Iso()
    display.FitAll()

def tabletop(event=None):
    pcd_file = open(os.path.join('assets', 'models', 'tabletop.pcd'), 'r').readlines()[11:]
    #create the point_cloud
    pc = Graphic3d_ArrayOfPoints(len(pcd_file), True)
    for idx, line in enumerate(pcd_file):
        x, y, z, rgb = map(float, line.split())
        rgb = float2int(rgb)
        r = (rgb >> 16 & 0x0000ff) / float(255)
        g = (rgb >> 8 & 0x0000ff) / float(255)
        b = (rgb & 0x0000ff) / float(255)
        color = Quantity_Color(r, g, b, Quantity_TOC_RGB)
        pc.AddVertex(gp_Pnt(x, y, z), color)

    point_cloud = AIS_PointCloud()
    point_cloud.SetPoints(pc.GetHandle())
    ais_context = display.GetContext().GetObject()
    ais_context.Display(point_cloud.GetHandle())
    display.DisableAntiAliasing()
    display.View_Iso()
    display.FitAll()

def float2int(flt):
    """
    Unpack PCL RGB data into r/g/b
    reference:
        http://docs.pointclouds.org/trunk/structpcl_1_1_point_x_y_z_r_g_b.html
        https://stackoverflow.com/questions/21106976/python-convert-a-signed-float-to-unsigned-long-dword-for-win32
    :param flt: float
    :return:    unsigned integer
    """
    return struct.unpack('I', struct.pack('f', flt))[0]
    #return struct.unpack('q', struct.pack('d', flt))[0]

if __name__ == '__main__':
    add_menu('pointcloud')
    add_function_to_menu('pointcloud', random_points)
    add_function_to_menu('pointcloud', bunny)
    add_function_to_menu('pointcloud', tabletop)
    start_display()
