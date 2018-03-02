# Set the active layer to the last art layer of the active document, or the
# first if the last is already active.

import win32com.client
# Start up Photoshop application
# app = win32com.client.Dispatch('Photoshop.Application')

# Or get Reference to already running Photoshop application instance
# app = win32com.client.GetObject(Class="Photoshop.Application")
app = win32com.client.GetActiveObject("Photoshop.Application")

if len(app.Documents) < 1:
    docRef = app.Documents.Add()
else:
    docRef = app.ActiveDocument

if len(docRef.Layers) < 2:
    docRef.ArtLayers.Add()

activeLayerName = docRef.ActiveLayer.Name
SetLayerName = ''

if docRef.ActiveLayer.Name != app.ActiveDocument.Layers.Item(len(docRef.Layers)).Name:
    docRef.ActiveLayer = docRef.Layers.Item(len(docRef.Layers))
else:
    docRef.ActiveLayer = docRef.Layers.Item(1)
