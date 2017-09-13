#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
Logic:
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: [1, .8]
            Graph:
                id: graph
                xlabel: ""
                ylabel: "Level"
        BoxLayout:
            size_hint: [1, .2]
            orientation: "horizontal"
            Button:
                text: "START"
                bold: True
                on_press: root.start()
            Button:
                text: "STOP"
                bold: True
                on_press: root.stop()