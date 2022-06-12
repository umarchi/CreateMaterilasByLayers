import rhinoscriptsyntax as rs

__commandname__ = "CreateMaterialsByLayers"

def RunCommand( is_interactive ):
  
  # Get layer names from recentfile
  allLayers = rs.LayerNames()
  num_layer = len(allLayers)
  
  # Select layers to make materials
  selectedLayers = rs.MultiListBox(allLayers, "Pick layers to make materials.")
  for selectedLayer in selectedLayers:
    
      # Check if the layers are applied the materials or not
      index = rs.LayerMaterialIndex(selectedLayer)
      
      # If the layers do not apply the materials
      if index == -1:
          rhino_material = rh.DocObjects.Material()
          rhino_material.Name = selectedLayer.replace("::","_")
          
          # Get layer color and apply it to layer material
          layer_color = System.Drawing.Color.ToArgb(rs.LayerPrintColor(selectedLayer))
          rhino_material.DiffuseColor = System.Drawing.Color.FromArgb(layer_color)
          
          # Create render materials
          render_material = rh.Render.RenderMaterial.CreateBasicMaterial(rhino_material)
          sc.doc.RenderMaterials.Add(render_material)
          
          # Apply materials to each layers
          for i in range(0,num_layer):
              if str(sc.doc.Layers[i].Id) == rs.LayerId(selectedLayer):
                sc.doc.Layers[i].RenderMaterial = render_material
  return 0
