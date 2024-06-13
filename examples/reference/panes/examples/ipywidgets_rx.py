# Original Source: https://github.com/opengeos/solara-geospatial/blob/main/pages/01_leafmap.py
import leafmap

from leafmap.toolbar import change_basemap

import panel as pn

from panel.ipywidget import create_rx

pn.extension("ipywidgets")

class Map(leafmap.Map):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add what you want below
        self.add_basemap("OpenTopoMap")
        change_basemap(self)


widget = Map(  # type: ignore
    zoom=2,
    center=(20,0),
    scroll_wheel_zoom=True,
    toolbar_ctrl=False,
    data_ctrl=False,
)

zoom, center = create_rx(widget, "zoom", "center")

layout = pn.Column(
    widget,
    # I would like to add a zoom_input widget created_from and synced to the zoom rx variable.
    # But its currently not possible in one line of code. See https://github.com/holoviz/panel/issues/6911
    zoom, center,
    pn.Row(
        pn.pane.Markdown(pn.rx("Zoom: {zoom}").format(zoom=zoom)),
        pn.pane.Markdown(pn.rx("Center: {center}").format(center=center)),
    ),
)

pn.template.FastListTemplate(
    site="🌎 Panel Geospatial",
    site_url="./",
    title="Leafmap",
    main=[layout],
    main_layout=None,
    accent="teal",
).servable()
