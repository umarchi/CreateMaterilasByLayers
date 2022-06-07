import rhinoscriptsyntax as rs

__commandname__ = "CreateMaterialsByLayers"

def RunCommand( is_interactive ):
  allLayers = rs.LayerNames()
  num_layer = len(allLayers)
  selectedLayers = rs.MultiListBox(allLayers, "Pick layers to make materials.")
  for selectedLayer in selectedLayers:
      index = rs.LayerMaterialIndex(selectedLayer)
      if index == -1:
          rhino_material = rh.DocObjects.Material()
          rhino_material.Name = selectedLayer.replace("::","_")
          layer_color = System.Drawing.Color.ToArgb(rs.LayerPrintColor(selectedLayer))
          rhino_material.DiffuseColor = System.Drawing.Color.FromArgb(layer_color)
          render_material = rh.Render.RenderMaterial.CreateBasicMaterial(rhino_material)
          sc.doc.RenderMaterials.Add(render_material)
          for i in range(0,num_layer):
              if str(sc.doc.Layers[i].Id) == rs.LayerId(selectedLayer):
                sc.doc.Layers[i].RenderMaterial = render_material
  return 0