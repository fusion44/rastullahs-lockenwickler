#/******************************************************************************************
#MOC - Minimal Ogre Collision v 1.0 beta
#The MIT License
#
#Copyright (c) 2008 MouseVolcano (Thomas Gradl, Esa Kylli, Erik Biermann, Karolina Sefyrin)
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#******************************************************************************************/

import ogre.renderer.OGRE as og

class CollisionTools:
    def __init__(self, sceneManager):
        self.sceneMgr = sceneManager
        self.raySceneQuery = self.sceneMgr.createRaySceneQuery(og.Ray())
        self.raySceneQuery.setSortByDistance(True)
        #self.heightAdjust = 0.0


    def raycastFromCamera(rw, camera, mouseEvent, result, target, closest_distance, queryMask = 0xFFFFFFFF):
        return

    def collidesWithEntity(fromPoint, toPoint, collisionRadius = 2.5, rayHeightLevel = 0.0, queryMask = 0xFFFFFFFF):
        return

    def calculateY(node, doGridCheck = True, gridWidth = 1.0, queryMask = 0xFFFFFFFF):
        return

    def raycastFromPoint( point, normal, result, target, closest_distance, queryMask = 0xFFFFFFFF):
        return

    def raycast( ray,  result, target, closest_distance, queryMask = 0xFFFFFFFF):
        return


    def GetMeshInformation(mesh, vertex_count, vertices, index_count, indices, position, orient, scale):
        return
