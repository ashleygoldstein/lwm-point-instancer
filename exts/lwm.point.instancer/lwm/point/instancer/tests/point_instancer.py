import omni.usd
from pxr import Usd, UsdGeom, Sdf, Gf


#Grab Stage
stage: Usd.Stage = omni.usd.get_context().get_stage()

#Define Point Instancer Path
prim_path = Sdf.Path("/World/Point_Instancer")

#Create Point Instancer on Stage at Path
instancer: UsdGeom.PointInstancer = UsdGeom.PointInstancer.Define(stage, prim_path)

#Create Prototypes Container/Folder
proto_container = UsdGeom.Scope.Define(stage, prim_path.AppendPath("Prototypes"))

#Create List
shapes = []

#Define number of duplicates
num_duplicates = 5

#Create cube and add to list
sphere = UsdGeom.Sphere.Define(stage, proto_container.GetPath().AppendPath("Sphere"))
shapes.append(sphere)

#Create prototype shapes
instancer.CreatePrototypesRel().SetTargets([shape.GetPath() for shape in shapes])

#Create Positions for each instance
positions = [Gf.Vec3f(i * 10, 0, 0) for i in range(num_duplicates)]
instancer.CreatePositionsAttr(positions)


#Create Proto Indices for spheres
instancer.CreateProtoIndicesAttr([0] * 5)